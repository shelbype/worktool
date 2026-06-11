from __future__ import annotations

from pathlib import PurePosixPath
from typing import Any
from urllib.parse import unquote, urlparse

import httpx

from ragbot.workflow import WechatBotAdapter


class HttpWechatBotAdapter(WechatBotAdapter):
    """WorkTool HTTP sender.

    WorkTool sends group text messages through sendRawMessage with robotId in
    the query string and a socketType/list body.
    """

    def __init__(self, api_base: str, robot_id: str, token: str = "") -> None:
        self.api_base = api_base.rstrip("/")
        self.robot_id = robot_id
        self.token = token

    def send_group_message(self, group_id: str, content: str, at_list: list[str] | None = None) -> dict[str, Any]:
        item: dict[str, object] = {
            "type": 203,
            "titleList": [group_id],
            "receivedContent": content,
        }
        if at_list:
            item["atList"] = at_list
        return self._post_raw_message(
            [item],
            timeout=10,
        )

    def send_group_image(self, group_id: str, image_url: str, caption: str | None = None) -> dict[str, Any]:
        item = {
            "type": 218,
            "titleList": [group_id],
            "objectName": self._object_name_from_url(image_url),
            "fileUrl": image_url,
            "fileType": "image",
        }
        if caption:
            item["extraText"] = caption
        return self._post_raw_message([item], timeout=15)

    def send_group_rich_message(self, group_id: str, content: str, image_urls: list[str]) -> dict[str, Any]:
        items = [
            {
                "type": 203,
                "titleList": [group_id],
                "receivedContent": content,
            }
        ]
        for image_url in image_urls:
            items.append(
                {
                    "type": 218,
                    "titleList": [group_id],
                    "objectName": self._object_name_from_url(image_url),
                    "fileUrl": image_url,
                    "fileType": "image",
                }
            )
        return self._post_raw_message(items, timeout=20)

    def update_callback(self, callback_url: str, reply_all: int = 1, open_callback: int = 1) -> dict[str, Any]:
        return self._post(
            "/robot/robotInfo/update",
            params={"robotId": self.robot_id},
            json={"openCallback": open_callback, "replyAll": reply_all, "callbackUrl": callback_url},
            timeout=10,
            action="WorkTool callback update",
        )

    def online(self) -> dict[str, Any]:
        return self._get("/robot/robotInfo/online", params={"robotId": self.robot_id}, timeout=10)

    def list_qa_logs(
        self,
        page: int = 1,
        size: int = 10,
        sort: str = "start_time,desc",
        name: str | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
    ) -> dict[str, Any]:
        return self._get(
            "/robot/qaLog/list",
            params={
                "robotId": self.robot_id,
                "page": page,
                "size": size,
                "sort": sort,
                "name": name,
                "startTime": start_time,
                "endTime": end_time,
            },
            timeout=10,
        )

    def list_raw_messages(
        self,
        message_id: str | None = None,
        page: int = 1,
        size: int = 10,
        sort: str = "create_time,desc",
    ) -> dict[str, Any]:
        return self._get(
            "/wework/listRawMessage",
            params={
                "robotId": self.robot_id,
                "messageId": message_id,
                "page": page,
                "size": size,
                "sort": sort,
            },
            timeout=10,
        )

    def list_raw_results(
        self,
        message_id: str | None = None,
        page: int = 1,
        size: int = 10,
        sort: str = "run_time,desc",
        start_time: str | None = None,
        end_time: str | None = None,
        raw_type: str | None = None,
    ) -> dict[str, Any]:
        return self._get(
            "/robot/rawMsg/list",
            params={
                "robotId": self.robot_id,
                "messageId": message_id,
                "page": page,
                "size": size,
                "sort": sort,
                "startTime": start_time,
                "endTime": end_time,
                "type": raw_type,
            },
            timeout=10,
        )

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _get(self, path: str, params: dict[str, object | None], timeout: float) -> dict[str, Any]:
        response = httpx.get(
            f"{self.api_base}{path}",
            params=self._clean_params(params),
            headers=self._headers(),
            timeout=timeout,
        )
        response.raise_for_status()
        data = response.json()
        self._ensure_success(data, f"WorkTool GET {path}")
        return data

    def _post(
        self,
        path: str,
        params: dict[str, object | None],
        json: dict[str, object],
        timeout: float,
        action: str,
    ) -> dict[str, Any]:
        response = httpx.post(
            f"{self.api_base}{path}",
            params=self._clean_params(params),
            headers=self._headers(),
            json=json,
            timeout=timeout,
        )
        response.raise_for_status()
        data = response.json()
        self._ensure_success(data, action)
        return data

    def _post_raw_message(self, items: list[dict[str, object]], timeout: float) -> dict[str, Any]:
        return self._post(
            "/wework/sendRawMessage",
            params={"robotId": self.robot_id},
            json={
                "socketType": 2,
                "list": items,
            },
            timeout=timeout,
            action="WorkTool sendRawMessage",
        )

    def _clean_params(self, params: dict[str, object | None]) -> dict[str, object]:
        return {key: value for key, value in params.items() if value is not None}

    def _ensure_success(self, data: Any, action: str) -> None:
        if not isinstance(data, dict):
            return
        code = data.get("code")
        if code is not None and code not in {0, 200}:
            raise RuntimeError(f"{action} failed: {data}")

    def _object_name_from_url(self, image_url: str) -> str:
        path = PurePosixPath(urlparse(image_url).path)
        name = unquote(path.name)
        if not name:
            return "image.jpg"
        if "." not in PurePosixPath(name).name:
            return f"{name}.jpg"
        return name

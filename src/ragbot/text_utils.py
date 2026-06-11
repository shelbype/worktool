from __future__ import annotations

import re


_LEADING_MENTION_RE = re.compile(r"^@.+?[\u2002-\u200a]\s*")
_KNOWN_LEADING_MENTIONS = ("@翁然", "@xclass AI")
_INVISIBLE_CHARS = str.maketrans("", "", "\u200b\u200c\u200d\ufeff")


def normalize_customer_text(text: str) -> str:
    text = _LEADING_MENTION_RE.sub("", text or "")
    for mention in _KNOWN_LEADING_MENTIONS:
        if text.startswith(mention):
            text = text[len(mention) :]
            break
    text = text.translate(_INVISIBLE_CHARS)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

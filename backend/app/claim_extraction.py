import re


SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def extract_claims(text: str) -> list[str]:
    cleaned = text.strip()
    if not cleaned:
        return []
    sentences = [s.strip() for s in SENTENCE_SPLIT.split(cleaned) if s.strip()]
    return sentences

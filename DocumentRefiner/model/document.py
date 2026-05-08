from dataclasses import dataclass

@dataclass(frozen=True)
class Document:
    data: str

EMPTY = Document("")
from dataclasses import dataclass

@dataclass(frozen=True)
class FileExtension:
    value: str

TEXT = FileExtension(".TXT")
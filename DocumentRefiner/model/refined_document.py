from dataclasses import dataclass
from DocumentRefiner.model.document import Document

@dataclass(frozen=True)
class RefinedDocument:
    document: Document
    refined_data: str
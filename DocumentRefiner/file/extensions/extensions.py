import pypdf
from docx import Document
from DocumentRefiner.file.model.extension import TEXT as TEXT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import PORTABLE_DOCUMENT_FORMAT as PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import DOCX as DOCX_FILE_EXTENSION

read_mode = "r"

class FileExtensions:
    @staticmethod
    def handle_file(normalized_file_path: str) -> list[str]:
        if normalized_file_path.endswith(TEXT_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_text_file__(normalized_file_path)

        if normalized_file_path.endswith(PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_portable_document_format_file__(normalized_file_path)

        if normalized_file_path.endswith(DOCX_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_docx_file__(normalized_file_path)

        return []

    @staticmethod
    def __handle_text_file__(normalized_file_path: str) -> list[str]:
        with open(normalized_file_path, read_mode) as file:
            return file.readlines()

    @staticmethod
    def __handle_portable_document_format_file__(normalized_file_path: str) -> list[str]:
        reader = pypdf.PdfReader(normalized_file_path)

        return [page.extract_text() for page in reader.pages]

    @staticmethod
    def __handle_docx_file__(normalized_file_path: str) -> list[str]:
        document = Document(normalized_file_path)

        return [paragraph.text for paragraph in document.paragraphs]
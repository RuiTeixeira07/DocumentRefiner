import pypdf
from docx import Document
from DocumentRefiner.file.model.extension import TEXT as TEXT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import PORTABLE_DOCUMENT_FORMAT as PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import DOCX as DOCX_FILE_EXTENSION
from DocumentRefiner.model.document import Document as DOCUMENT
from DocumentRefiner.model.document import EMPTY as DOCUMENT_EMPTY

read_mode = "r"
line_feed = "\n"

class FileExtensions:
    @staticmethod
    def handle_file(normalized_file_path: str) -> DOCUMENT:
        if normalized_file_path.endswith(TEXT_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_text_file__(normalized_file_path)

        if normalized_file_path.endswith(PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_portable_document_format_file__(normalized_file_path)

        if normalized_file_path.endswith(DOCX_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_docx_file__(normalized_file_path)

        return DOCUMENT_EMPTY

    @staticmethod
    def __handle_text_file__(normalized_file_path: str) -> DOCUMENT:
        with open(normalized_file_path, read_mode) as file:
            return DOCUMENT(file.read())

    @staticmethod
    def __handle_portable_document_format_file__(normalized_file_path: str) -> DOCUMENT:
        reader = pypdf.PdfReader(normalized_file_path)

        return DOCUMENT(line_feed.join([page.extract_text() for page in reader.pages]))

    @staticmethod
    def __handle_docx_file__(normalized_file_path: str) -> DOCUMENT:
        document = Document(normalized_file_path)

        return DOCUMENT(line_feed.join([paragraph.text for paragraph in document.paragraphs]))
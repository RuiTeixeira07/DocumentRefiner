import re
from DocumentRefiner.model.document import Document
from DocumentRefiner.model.refined_document import RefinedDocument
from DocumentRefiner.resources.extensions.string import StringExtensions
from DocumentRefiner.resources.format.format import Format
from DocumentRefiner.resources.model.line_ending import CARRIAGE_RETURN, LINE_FEED, END_OF_LINE

pagination = fr"(\d)+/(\d)+({CARRIAGE_RETURN.value}|{LINE_FEED.value}|{END_OF_LINE.value})"

class Refiner:
    @staticmethod
    def refine(
        document: Document,
        remove_consecutive_whitespace_characters: bool = True,
        remove_blank_lines: bool = True,
        remove_consecutive_paragraphs: bool = True,
        remove_leading_artifacts: bool = True,
        remove_trailing_artifacts: bool = True,
        remove_pagination: bool = True) -> RefinedDocument:

        if (remove_consecutive_whitespace_characters
            and remove_blank_lines
            and remove_consecutive_paragraphs
            and remove_leading_artifacts
            and remove_trailing_artifacts
            and remove_pagination):
            return RefinedDocument(document, Refiner.remove_pagination(Format.clean_text(document.data)))

        data = document.data

        if remove_consecutive_whitespace_characters:
            data = StringExtensions.remove_consecutive_whitespace_characters(data)

        if remove_blank_lines:
            data = StringExtensions.remove_blank_lines(data)

        if remove_consecutive_paragraphs:
            data = StringExtensions.remove_consecutive_paragraphs(data)

        if remove_leading_artifacts:
            data = StringExtensions.remove_leading_artifacts(data)

        if remove_trailing_artifacts:
            data = StringExtensions.remove_trailing_artifacts(data)

        if remove_pagination:
            data = Refiner.remove_pagination(data)

        return RefinedDocument(document, data)

    @staticmethod
    def remove_pagination(text: str) -> str:
        return re.sub(pagination, "", text)
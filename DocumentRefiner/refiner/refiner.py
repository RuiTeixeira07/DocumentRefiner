from DocumentRefiner.resources.extensions.string import StringExtensions
from DocumentRefiner.resources.format.format import Format

class Refiner:
    @staticmethod
    def refine(
        data: str,
        remove_consecutive_whitespace_characters: bool = True,
        remove_blank_lines: bool = True,
        remove_consecutive_paragraphs: bool = True,
        remove_leading_artifacts: bool = True) -> str:

        if (remove_consecutive_whitespace_characters
            and remove_blank_lines
            and remove_consecutive_paragraphs
            and remove_leading_artifacts):
            return Format.clean_text(data)

        if remove_consecutive_whitespace_characters:
            data = StringExtensions.remove_consecutive_whitespace_characters(data)

        if remove_blank_lines:
            data = StringExtensions.remove_blank_lines(data)

        if remove_consecutive_paragraphs:
            data = StringExtensions.remove_consecutive_paragraphs(data)

        if remove_leading_artifacts:
            data = StringExtensions.remove_leading_artifacts(data)

        return data
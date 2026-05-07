from DocumentRefiner.resources.extensions.string import StringExtensions
from DocumentRefiner.resources.format.format import Format

class Refiner:
    @staticmethod
    def refine(
        data: str,
        remove_consecutive_whitespace_characters: bool = True,
        remove_blank_lines: bool = True) -> str:

        if (remove_consecutive_whitespace_characters
            and remove_blank_lines):
            return Format.clean_text(data)

        if remove_consecutive_whitespace_characters:
            data = StringExtensions.remove_consecutive_whitespace_characters(data)

        if remove_blank_lines:
            data = StringExtensions.remove_blank_lines(data)

        return data
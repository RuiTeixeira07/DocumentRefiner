import re
from DocumentRefiner.resources.model.line_ending import CARRIAGE_RETURN, LINE_FEED, END_OF_LINE

two_consecutive_paragraphs = f"({CARRIAGE_RETURN.value}|{LINE_FEED.value}|{END_OF_LINE.value}){{2,}}"

empty_line= 2 * LINE_FEED.value

whitespace_character = " "
two_consecutive_whitespace_characters = f"({whitespace_character}){{2,}}"

blank_lines = f"({whitespace_character})+({CARRIAGE_RETURN.value}|{LINE_FEED.value}|{END_OF_LINE.value})"

class StringExtensions:
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean text.
        Order of operations is deliberate.

        :param str text: The text to be cleaned.
        :return: Cleaned text.
        """
        text = StringExtensions.remove_consecutive_whitespace_characters(text)
        text = StringExtensions.remove_blank_lines(text)
        text = StringExtensions.remove_consecutive_paragraphs(text)

        text = StringExtensions.remove_leading_artifacts(text)
        text = StringExtensions.remove_trailing_artifacts(text)

        return text

    @staticmethod
    def remove_leading_artifacts(text: str) -> str:
        text = StringExtensions.__remove_leading_elements__(text, CARRIAGE_RETURN.value)
        text = StringExtensions.__remove_leading_elements__(text, LINE_FEED.value)
        text = StringExtensions.__remove_leading_elements__(text, END_OF_LINE.value)
        text = StringExtensions.__remove_leading_elements__(text, whitespace_character)

        return text

    @staticmethod
    def remove_trailing_artifacts(text: str) -> str:
        text = StringExtensions.__remove_trailing_elements__(text, CARRIAGE_RETURN.value)
        text = StringExtensions.__remove_trailing_elements__(text, LINE_FEED.value)
        text = StringExtensions.__remove_trailing_elements__(text, END_OF_LINE.value)
        text = StringExtensions.__remove_trailing_elements__(text, whitespace_character)

        return text

    @staticmethod
    def remove_consecutive_paragraphs(text: str) -> str:
        return re.sub(two_consecutive_paragraphs, empty_line, text)

    @staticmethod
    def remove_blank_lines(text: str) -> str:
        return re.sub(blank_lines, LINE_FEED.value, text)

    @staticmethod
    def remove_consecutive_whitespace_characters(text: str) -> str:
        return re.sub(two_consecutive_whitespace_characters, whitespace_character, text)

    @staticmethod
    def __remove_leading_elements__(text: str, element: str) -> str:
        return text[len(element):] if text[:len(element)] == element else text

    @staticmethod
    def __remove_trailing_elements__(text: str, element: str) -> str:
        return text[:-len(element)] if text[-len(element):] == element else text
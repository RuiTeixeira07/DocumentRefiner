import re

carriage_return = "\r"
line_feed = "\n"
end_of_line = carriage_return + line_feed
two_consecutive_paragraphs = f"({carriage_return}|{line_feed}|{end_of_line}){{2,}}"

empty_line= 2 * line_feed

whitespace_character = " "
two_consecutive_whitespace_characters = f"[{whitespace_character}]{{2,}}"

blank_lines = f"[{whitespace_character}]+({carriage_return}|{line_feed}|{end_of_line})"

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
        text = StringExtensions.__remove_leading_elements__(text, carriage_return)
        text = StringExtensions.__remove_leading_elements__(text, line_feed)
        text = StringExtensions.__remove_leading_elements__(text, end_of_line)
        text = StringExtensions.__remove_leading_elements__(text, whitespace_character)

        return text

    @staticmethod
    def remove_trailing_artifacts(text: str) -> str:
        text = StringExtensions.__remove_trailing_elements__(text, carriage_return)
        text = StringExtensions.__remove_trailing_elements__(text, line_feed)
        text = StringExtensions.__remove_trailing_elements__(text, end_of_line)
        text = StringExtensions.__remove_trailing_elements__(text, whitespace_character)

        return text

    @staticmethod
    def remove_consecutive_paragraphs(text: str) -> str:
        return re.sub(two_consecutive_paragraphs, empty_line, text)

    @staticmethod
    def remove_blank_lines(text: str) -> str:
        return re.sub(blank_lines, line_feed, text)

    @staticmethod
    def remove_consecutive_whitespace_characters(text: str) -> str:
        return re.sub(two_consecutive_whitespace_characters, whitespace_character, text)

    @staticmethod
    def __remove_leading_elements__(text: str, element: str) -> str:
        return text[len(element):] if text[:2] == element else text

    @staticmethod
    def __remove_trailing_elements__(text: str, element: str) -> str:
        return text[:-len(element)] if text[-len(element):] == element else text
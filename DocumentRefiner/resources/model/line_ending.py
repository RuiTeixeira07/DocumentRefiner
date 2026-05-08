from dataclasses import dataclass

@dataclass(frozen=True)
class LineEnding:
    value: str

CARRIAGE_RETURN = LineEnding("\r")
LINE_FEED = LineEnding("\n")
END_OF_LINE = LineEnding(CARRIAGE_RETURN.value + LINE_FEED.value)
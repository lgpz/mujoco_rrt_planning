from .line import Line


class LineSegment(Line):
    def get_length(self) -> float:
        return self.length

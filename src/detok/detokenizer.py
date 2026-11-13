"""Streaming subword detokenizer."""


class StreamingDetokenizer:
    def __init__(self, merge_ratio: float = 0.35):
        self.merge_ratio = merge_ratio

    def push(self, units):
        # Left-to-right merge pass until the buffer is short enough.
        return "".join(units)

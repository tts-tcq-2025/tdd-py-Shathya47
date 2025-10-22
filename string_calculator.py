class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiter, numbers = self._extract_delimiter(numbers)
        parts = self._parse_numbers(numbers, delimiter)
        self._raise_for_negatives(parts)
        return self._sum_ignoring_large(parts)

    def _extract_delimiter(self, text: str) -> tuple[str, str]:
        """Extract custom or default delimiter."""
        if not text.startswith("//"):
            return ",", text

        header, text = text.split("\n", 1)
        # Handle multi-character or single-character delimiters separately
        if "[" in header:
            return self._extract_multi_delimiter(header), text
        return self._extract_single_delimiter(header), text

    def _extract_single_delimiter(self, header: str) -> str:
        """Extract single-character delimiter like //;\n"""
        return header[2:]

    def _extract_multi_delimiter(self, header: str) -> str:
        """Extract multi-character delimiter like //[***]\n"""
        return header[header.find("[") + 1 : header.find("]")]

    def _parse_numbers(self, text: str, delimiter: str) -> list[int]:
        """Normalize newlines, split, and convert to integers."""
        return [int(x) for x in text.replace("\n", delimiter).split(delimiter) if x]

    def _raise_for_negatives(self, numbers: list[int]) -> None:
        """Raise error listing negatives, if any."""
        negatives = list(filter(lambda n: n < 0, numbers))
        if not negatives:
            return
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    def _sum_ignoring_large(self, numbers: list[int]) -> int:
        """Return sum ignoring numbers >1000."""
        return sum(n for n in numbers if n <= 1000)

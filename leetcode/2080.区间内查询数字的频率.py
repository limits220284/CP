class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dct = defaultdict(list)
        for i, v in enumerate(arr): self.dct[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect.bisect_right(self.dct[value], right) - bisect.bisect_left(self.dct[value], left)
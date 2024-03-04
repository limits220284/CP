class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        s = Counter()
        for x,y in items1:
            s[x] += y
        for x,y in items2:
            s[x] += y
        return sorted(s.items())
        
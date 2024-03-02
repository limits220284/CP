class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        cnt = 0
        for x, y in pairwise(s):
            if x != y:
                cnt += 1
        return cnt
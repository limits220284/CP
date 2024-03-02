class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for a, b in operations:
            t = gem[a] // 2
            gem[a] -= t
            gem[b] += t
        return max(gem) - min(gem)
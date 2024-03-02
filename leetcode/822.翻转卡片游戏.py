class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        forbid = {fronts[i] for i in range(n) if fronts[i] == backs[i]}
        res = inf
        for num in chain(fronts, backs):
            if num not in forbid:
                res = min(res, num)
        return res if res is not inf else 0
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = set()
        tmp = set()
        for x in arr:
            tmp = {x & o for o in tmp}
            tmp.add(x)
            ans |= tmp
        return min(abs(x - target) for x in ans)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 二分
        def check(mid):
            res = 0
            for x in citations:
                if x >= mid:
                    res += 1
            return res
        l, r = 0, max(citations)
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid) >= mid:
                l = mid
            else:
                r = mid - 1
        return l
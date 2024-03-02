class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 设计对数时间复杂度
        # 二分h
        # 从0-n
        n = len(citations)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if n - mid <= citations[mid]:
                r = mid
            else:
                l = mid + 1
        # 
        if n - l <= citations[l]:
            return n - l
        return 0
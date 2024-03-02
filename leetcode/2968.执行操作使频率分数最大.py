class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0]
        for x in nums:
            prefix.append(x + prefix[-1])
        def check(mid):
            for i in range(n):
                if i < mid - 1:
                    continue
                zj = nums[(i - mid + 1 + i) // 2]
                idx = (i - mid + 1 + i) // 2
                need = zj * (idx - (i - mid + 1) + 1) - (prefix[idx + 1] - prefix[i - mid + 1])
                need += (prefix[i + 1] - prefix[idx]) - (zj * (i - idx + 1))
                if need <= k:
                    return True
            return False
            
        l, r = 0, n
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
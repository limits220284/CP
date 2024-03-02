from sortedcontainers import SortedList
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # 前后缀分解
        n = len(nums)
        left = [None for _ in range(n)]
        tot = 0
        mx = 0
        idx = 0
        for i in range(n):
            if i < k - 1:
                tot += nums[i]
                continue
            tot += nums[i]
            # 计算出最大值的下标组
            if tot > mx:
                mx = tot
                idx = i - k + 1
            left[i] = [mx, idx]
            tot -= nums[i - k + 1]
        print(left)
        right = [None for _ in range(n)]
        tot = 0
        mx = 0
        idx = 0
        for i in range(n - 1, -1, -1):
            if i > n - k:
                tot += nums[i]
                continue
            tot += nums[i]
            # 计算出最大值的下标组
            if tot >= mx:
                mx = tot
                idx = i
            right[i] = [mx, idx]
            tot -= nums[i + k - 1]
        print(right)
        tot = 0
        mx = 0
        ans = None
        for i in range(n - k):
            # 如果要保证不重叠，要保证 i - k + 1 > k
            if i < k - 1:
                tot += nums[i]
                continue
            tot += nums[i]
            if i >= 2 * k - 1:
                if left[i - k][0] + tot + right[i + 1][0] > mx:
                    ans = [left[i - k][1], i - k + 1, right[i + 1][1]]
                    mx = left[i - k][0] + tot + right[i + 1][0]
            tot -= nums[i - k + 1]
        return ans

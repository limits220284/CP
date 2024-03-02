class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        # 双倍即可
        ss = sum(nums)
        rest = 0
        if target > ss:
            rest += target // ss
            target = target % ss
        arr = nums + nums
        n = len(arr)
        l = 0
        tot = 0
        ans = inf
        for r in range(n):
            tot += arr[r]
            while tot > target:
                tot -= arr[l]
                l += 1
            if tot == target:
                ans = min(ans, r - l + 1)
        return -1 if ans == inf else ans + rest * len(nums)
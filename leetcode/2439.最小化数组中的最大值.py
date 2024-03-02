class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # 最大值最小，直接二分
        n = len(nums)
        l, r = 0, max(nums)
        def check(mid):
            arr = nums[::]
            for i in range(n - 1, 0, -1):
                if arr[i] > mid:
                    dif = arr[i] - mid
                    arr[i] -= dif
                    arr[i-1] += dif
            return arr[0] <= mid
        return bisect_left(range(max(nums)), True, key = check)
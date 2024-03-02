class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # 一眼二分
        # 二分最大差值，每次选取mid
        # check()函数怎么写？
        # 判断在最大差值为mid的情况下能否找到p对不同的下标对
        # f[i]表示以i结尾的满足小于mid的最长长度
        # 打家劫舍1
        # f[i] = max(f[i - 1], f[i - 2] + tmp[i])
        nums.sort()
        arr = [y - x for x, y in pairwise(nums)]
        n = len(arr)
        def check(mid):
            tmp = [1 if x <= mid else 0 for x in arr]
            f = [0] * (n + 2)
            for i in range(2, n + 2):
                f[i] = max(f[i - 1], f[i - 2] + tmp[i - 2])
            return f[-1]
        return bisect_left(range(0, nums[-1] - nums[0]), p,  key = check)
        # l, r = 0, max(nums) - min(nums)
        # while l < r:
        #     mid = (l + r) // 2
        #     if check(mid):
        #         r = mid
        #     else:
        #         l = mid + 1
        # return l
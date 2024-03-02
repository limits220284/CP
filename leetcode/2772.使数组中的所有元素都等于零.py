class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        # 差分数组
        n = len(nums)
        f = [nums[0]] + [0] * n
        for i in range(1, n):
            f[i] = nums[i] - nums[i-1]
        print(f)
        f = [0] + f
        for i in range(n - k + 1):
            x = f[i] + f[i+1]
            if x < 0: return False
            f[i+1] = 0
            f[i+1+k] += x
        print(f)
        for i in range(1, n+1):
            if f[i] != 0 :
                return False
        return True
        
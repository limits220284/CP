class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        # 与运算只会使得分数变小
        # 如果不到零就一直与，直到为零
        n = len(nums)
        pre = nums[0]
        cnt = 0
        flag = False
        for i in range(1, n):
            if pre == 0:
                cnt += 1
                pre = nums[i]
                flag = True
            else:
                pre = pre & nums[i]
        if pre != 0 and flag:
            return cnt
        return cnt + 1
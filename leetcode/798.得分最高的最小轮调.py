class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        move = [0] * n
        for i, x in enumerate(nums):
            if x <= i:
                move[0] += 1
                move[(i + 1) % n] += 1
                move[(i - nums[i] + 1) % n] -= 1
            else:
                move[(i + 1) % n] += 1
                move[(n - nums[i] + i + 1) % n] -= 1
        ss = 0
        mx = 0
        ans = 0
        for k, m in enumerate(move):
            ss += m
            if ss > mx:
                ss = mx
                ans = k
        return ans
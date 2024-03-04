class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # 贪心,正数都在前面,[2,3,1,-1,-3,0,-3]
        nums.sort(reverse = True)
        arr = [0]
        for x in nums:
            arr.append(arr[-1]+x)
        arr.pop(0)
        ans = 0
        for x in arr:
            if x>0:
                ans += 1
        return ans
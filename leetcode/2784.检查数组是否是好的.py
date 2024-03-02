class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1
        ans = []
        for i in range(n):
            ans.append(i+1)
        ans.append(n)
        # print(ans)
        return ans == sorted(nums)
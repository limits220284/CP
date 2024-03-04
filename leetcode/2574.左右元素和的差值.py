class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        n = len(nums)
        for i in range(n):
            left.append(left[-1]+nums[i])
        right=[0]
        for i in range(n-1,-1,-1):
            right.append(right[-1]+nums[i])
        right.reverse()
        print(left,right)
        ans = []
        for i in range(n):
            ans.append(abs(left[i+1]-right[i]))
        return ans
                       
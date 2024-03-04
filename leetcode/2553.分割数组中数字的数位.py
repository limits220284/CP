class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            x=str(x)
            for c in x:
                ans.append(int(c))
        return ans
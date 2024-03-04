class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        s=Counter(nums)
        ans=[0]*2
        for x in s:
            ans[0]+=s[x]//2
            ans[1]+=s[x]%2
        return ans
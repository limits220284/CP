class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # hash表记录
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        def rev(x):
            ans=0
            while x:
                ans=ans*10+x%10
                x//=10
            return ans
        dic=defaultdict(int)
        ans=0
        for x in nums:
            k=x-rev(x)
            if k in dic:
                ans+=dic[k]
            dic[k]+=1
        return ans%(10**9 + 7)

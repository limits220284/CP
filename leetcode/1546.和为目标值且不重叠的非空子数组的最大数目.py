class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        #贪心的思路
        arr=[0]
        for x in nums:
            arr.append(x+arr[-1])
        ans=0
        dic=Counter()
        for x in arr:
            if x-target in dic:
                ans+=1
                dic.clear()
            dic[x]+=1
        return ans
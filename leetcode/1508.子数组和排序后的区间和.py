class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new=[]
        for i in range(n):
            cnt=0
            for j in range(i,n):
                cnt+=nums[j]
                new.append(cnt)
        new.sort()
        return sum(new[left-1:right])%(10**9+7)
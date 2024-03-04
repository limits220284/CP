class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # 纯纯暴力？
        ans=[]
        for i,j in zip(l,r):
            if j==i:
                ans.append(True)
                continue
            tmp=nums[i:j+1][::]
            tmp.sort()
            k=tmp[1]-tmp[0]
            flag=True
            for x,y in pairwise(tmp):
                if y-x!=k:
                    flag=False
            ans.append(flag)
        return ans

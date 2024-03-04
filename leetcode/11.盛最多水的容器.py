class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i,j=0,n-1
        res=-1
        while i<j:
            res=max(res,(j-i)*min(height[i],height[j]))
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return res

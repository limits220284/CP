class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        #可以采用单调栈
        mx=0
        cnt=0
        for i in range(len(arr)):
            mx=max(arr[i],mx)
            if mx==i:
                cnt+=1
        return cnt
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        #hash表做法
        n=len(hours)
        arr=[0]
        for i in range(n):
            arr.append(arr[-1]+(1 if hours[i]>8 else -1))
        dic={}
        ans=0
        print(arr)
        for i in range(1,n+1):
            if arr[i]>0:
                ans=i
            else:
                if arr[i]-1 in dic:
                    ans=max(ans,i-dic[arr[i]-1])
                if arr[i] not in dic:
                    dic[arr[i]]=i
        return ans
            
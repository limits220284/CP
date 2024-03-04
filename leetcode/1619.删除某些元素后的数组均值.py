class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        d=int(n*0.05)
        arr.sort()
        s=0
        for i in range(d,n-d):
            s+=arr[i]
        return s/(n-2*d)
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        arr=[0]*46
        for i in range(lowLimit,highLimit+1):
            cnt=0
            while i:
                cnt+=i%10
                i//=10
            arr[cnt]+=1
        return max(arr)
            
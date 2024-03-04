class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        mi, mx = 0, 0
        arr = nums[::]
        for i in range(1,n,2):
            t = arr[i-1]
            if i != n-1:
                t = min(arr[i+1], t)
            if arr[i] >= t:
                mi += arr[i] - t + 1
        for i in range(1,n,2):
            if arr[i-1] >= arr[i]:
                mx += arr[i-1] - arr[i] + 1
            if i != n-1 and arr[i+1] >= arr[i]:
                mx += arr[i+1] - arr[i] + 1
                arr[i+1] = arr[i] - 1
        return min(mx, mi)
            

                

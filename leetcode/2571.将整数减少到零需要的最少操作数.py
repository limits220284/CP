class Solution:
    def minOperations(self, v: int) -> int:
        arr = [int(i) for i in bin(v)[2:]]
        arr = [0] + arr
        n = len(arr)
        arr.reverse()
        l, r = 0, 0
        ans = 0
        while r < n:
            if arr[r] == 0:
                r += 1
                l += 1
                continue
            while r < n and arr[r]:
                r+=1
            if r - l >= 2:
                arr[r] = 1
            ans += 1
            l = r
        return ans
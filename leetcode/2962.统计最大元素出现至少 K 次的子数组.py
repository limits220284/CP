class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)
        mxidx = []
        for i, x in enumerate(nums):
            if x == mx:
                mxidx.append(i)
        # print(mxidx)
        m = len(mxidx)
        l, r = 0, k - 1
        ans = 0
        while r < m:
            ll = mxidx[l] + 1
            if r + 1 < m:
                rr = mxidx[r + 1] - mxidx[r]
            else:
                rr = n - mxidx[r]
            ans += ll * rr
            l += 1
            r += 1
        return ans
                
            
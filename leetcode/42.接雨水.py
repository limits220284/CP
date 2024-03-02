class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0] * n
        mx = 0
        for i in range(n):
            mx = max(mx, height[i])
            l[i] = mx
        mx = 0
        r = [0] * n
        for i in range(n-1, -1, -1):
            mx = max(mx, height[i])
            r[i] = mx
        ans = 0
        for i in range(n):
            ans += (max(0, min(l[i], r[i]) - height[i]))
        return ans
        
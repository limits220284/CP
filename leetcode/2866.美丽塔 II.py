class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        pre = [0] * (n+1)
        suf = [0] * (n+1)
        stk = [0]
        for i in range(n):
            x = maxHeights[i]
            while len(stk) > 1 and maxHeights[stk[-1]-1] > x:
                stk.pop()
            pre[i+1] = (i+1 - stk[-1]) * x + pre[stk[-1]]
            stk.append(i+1)
        stk = [n]
        for i in range(n-1, -1, -1):
            x = maxHeights[i]
            while len(stk) > 1 and maxHeights[stk[-1]] > x:
                stk.pop()
            suf[i] = (stk[-1] - i) * x + suf[stk[-1]]
            stk.append(i)
        ans = 0
        for i in range(n):
            ans = max(ans, pre[i+1] + suf[i] - maxHeights[i])
        return ans
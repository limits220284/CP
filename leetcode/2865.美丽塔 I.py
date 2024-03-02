class Solution:
    def maximumSumOfHeights(self, mh: List[int]) -> int:
        # 枚举峰值
        n = len(mh)
        ans = 0
        for t in range(n):
            tot = mh[t]
            # print(tot)
            i, j = t-1, t+1
            pre = tot
            while i >= 0:
                cur = min(pre, mh[i])
                # print(i, cur)
                tot += cur
                pre = cur
                i -= 1
            pre = tot
            while j < n:
                cur = min(pre, mh[j])
                # print(j, cur)
                tot += cur
                pre = cur
                j += 1
            ans = max(ans, tot)
        return ans
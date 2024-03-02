class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        # 枚举y
        # 然后枚举d
        # 找到对应的在这个区间内的x的个数
        # cnt[y] * d * cnt[x]即可j
        mod = 10 ** 9 + 7
        mx = max(nums)
        cnt = [0] * (1 + mx)
        for x in nums:
            cnt[x] += 1
        pre = [0]
        for x in cnt[1:]:
            pre.append(x + pre[-1])
        ans = 0
        for y in range(1, mx + 1):
            if cnt[y]:
                d = 1
                while d * y <= mx:
                    ans += (d * cnt[y] * (pre[min((d + 1) * y - 1, mx)] - pre[d * y - 1]))
                    d += 1
                    ans %= mod
        return ans
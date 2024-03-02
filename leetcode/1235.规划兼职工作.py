#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#

# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def cmp(x):
            return x[1]
        # 二分找到离该段最近的段，看距离最大值是多少，通过hash表进行保存
        n = len(startTime)
        seps = list(zip(startTime, endTime, profit))
        seps.sort(key = lambda x: x[1])
        f = defaultdict(int)
        ans = 0
        for sep in seps:
            s, e, p = sep
            l = bisect_right(seps, s, key = cmp)
            if s < seps[l-1][1]:
                f[e] = max(f[e], f[s] + p)
            else:
                f[e] = max(f[e], f[seps[l-1][1]] + p)
            # 同时需要找到end左边最接近他的，然后取一个最大值
            l = bisect_left(seps, e, key = cmp)
            if e > seps[l-1][1]:
                f[e] = max(f[e], f[seps[l-1][1]])
            ans = max(f[e], ans)
        print(f)
        return ans


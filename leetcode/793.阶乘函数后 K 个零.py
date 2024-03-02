class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # 存在的5有多少个，零就有多少个，因为2的个数永远比5的个数多
        # 统计多少个数的阶乘末尾为k个零，实际求的是存在多少个数包含k个因子5
        # 0 <= k <= 1e9
        # 需要找到多少个数中包括这么多的5
        # 1！：0 2！：0 3！：0 4！：0 5！：1 6！：1 7！：1 8！：1 9！：1 10！：2
        # 5 10 15 20 25（到25的时候一次性增加了两个）
        # f(x) 是单调递增的，所以可以采用二分查找进行求解
        # 存在上界和下界
        # 一个比较弱的上界限
        # 假设存在k个5都是单因子，那么最大的数就是5(k + 1)
        mx = 5 * (k + 1)
        def check(x):
            cnt = 0
            while x != 0:
                x //= 5
                cnt += x
            return cnt
        l, r = 0, mx
        while l < r:
            mid = (l + r) // 2
            if check(mid) >= k:
                r = mid
            else:
                l = mid + 1
        al = l
        l, r = 0, mx
        while l < r:
            mid = (l + r) // 2
            if check(mid) >= k + 1:
                r = mid
            else:
                l = mid + 1
        return l - al
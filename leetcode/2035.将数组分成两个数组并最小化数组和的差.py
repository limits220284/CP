class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # 左边一半按着数量进行分类，计算出来所有的结果
        # 然后枚举右边的结果, 如果右边只有一个数字，那么左边就是n//2-1个数字里面选
        # 选的结果是什么呢？对应的arr，tot = l + r + res
        # abs(l + r - res) = abs(l + r - tot + l + r) = abs(2l + 2r - tot)
        # 采用状态空间进行优化
        s = sum(nums)
        n = len(nums)
        m = n // 2
        f = defaultdict(list)
        for i in range(1 << m):
            tot, t = 0, 0
            k = i
            while k:
                lb = k & -k
                k -= lb
                tot += nums[lb.bit_length()-1]
                t += 1
            f[t].append(tot)
        for k in f.keys():
            f[k].sort()
        ans = inf
        for i in range(1 << m):
            tot, t = 0, 0
            k = i
            while k:
                lb = k & -k
                k -= lb
                tot += nums[lb.bit_length()-1 + m]
                t += 1
            arr = f[m-t]
            idx = bisect_left(arr, (s - 2 * tot) // 2)
            if idx > 0: ans = min(ans, abs(2 * arr[idx-1] + 2 * tot - s))
            if idx < len(arr): ans = min(ans, abs(2 * arr[idx] + 2 * tot - s))
        return ans


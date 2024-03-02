class Solution:
    def splitArraySameAverage1(self, nums: List[int]) -> bool:
        n = len(nums)
        m = n // 2
        s = sum(nums)
        # sum(A) = (sum(nums) * k) / n
        # o(n)进行判断是否合适
        if all(s * i % n for i in range(1, m + 1)):
            return False
        # f[i][x]表示遍历过的元素中可以取出i个元素构成的和为x
        # f[i][x] = f[i-1][x-nums[j]]
        f = [set() for _ in range(m+1)]
        f[0].add(0)
        for i in range(n):
            for j in range(m, 0, -1):
                for x in f[j-1]:
                    curr = x + nums[i]
                    if curr * n == s * j:
                        return True
                    f[j].add(curr)
        return False
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s

        m = n // 2
        left = set()
        for i in range(1, 1 << m):
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0:
                return True
            left.add(tot)

        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
            if tot == 0 or rsum != tot and -tot in left:
                return True
        return False
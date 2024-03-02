"""
f[i][j] 表示到f[i][j]时，等于目标和的非空子矩阵的数量
如果是一维的，那么只用维护一下前缀和，然后遍历前缀和，采用hash表计数即可
二维的应该也是这个思路
写一下二维的公式
d  - c - b + a = target
只知道一个d，只知道一个target
d - target = b + c - a
可以知道的是，b + c - a就是两条长方形
"""
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        def work(nums):
            res = 0
            cnt = Counter()
            pre = [0]
            for x in nums: pre.append(x + pre[-1])
            for i, x in enumerate(pre):
                res += cnt[x - target]
                cnt[x] += 1
            return res


        ans = 0
        for i in range(m):
            tot = [0] * n
            for j in range(i, m):    
                for k in range(n):
                    tot[k] += matrix[j][k]
                ans += work(tot)
        return ans
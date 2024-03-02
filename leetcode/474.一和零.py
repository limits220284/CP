class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # f[i][j][k] 表示前i个数中，不超过j个0和k个1的最大子集长度
        # f[i][j][k] = max(f[i-1][j][k], f[i-1][j-num0][k-num1])
        ls = len(strs)
        f = [[[0] * (n+1) for _ in range(m+1)] for _ in range(ls + 1)]
        for i in range(1, ls + 1):
            num0 = strs[i-1].count('0')
            num1 = strs[i-1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    f[i][j][k] = f[i-1][j][k]
                    if j >= num0 and k >= num1:
                        f[i][j][k] = max(f[i-1][j][k], f[i-1][j-num0][k-num1] + 1)
        return f[-1][-1][-1]
class Solution:
    def numTrees(self, n: int) -> int:
        f = [0] * (n+1)
        f[0] = f[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                f[i] += f[j-1] * f[i - j]
        return f[n]
        # c = 1
        # for i in range(n):
        #     c = c * 2 * (2 * i + 1) / (i+2)
        # return int(c)
        # 

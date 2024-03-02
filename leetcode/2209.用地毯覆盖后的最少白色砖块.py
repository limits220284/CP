"""
直接dp起手
状态定义:
题目要求什么就定义什么，需要把握住变量的关系
一个是砖块长度，一个是地毯数量
f[i][j]就是用i块地毯覆盖前j块砖块后，没有被覆盖的白色砖块的最少数目

状态转移:
考虑是否使用第i条地毯覆盖第j块板砖
不使用: f[i][j] = f[i][j-1] + (floor[j] == 1)
使用: f[i][j] = f[i-1][j - carpetLen]
两者使用最小值即可

"""

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        f = [[0] * n for _ in range(numCarpets + 1)]
        cnt1 = 0
        for i in range(n):
            cnt1 += (floor[i] == '1')
            f[0][i] = cnt1
        for i in range(1, numCarpets + 1):
            for j in range(1, n):
                # 不使用
                f[i][j] = f[i][j-1] + (floor[j] == '1') 
                if j >= carpetLen:
                    f[i][j] = min(f[i][j], f[i-1][j - carpetLen])
                else:
                    f[i][j] = 0
        # print(f)
        return f[numCarpets][n - 1]
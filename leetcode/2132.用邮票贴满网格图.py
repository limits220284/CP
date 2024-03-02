# 既然能够覆盖，那只需要保证某个区域只需要长和宽大于邮票长和宽即可
# 那就需要计算出非占有区域的
# 遍历 + 二维前缀和
# 枚举右下角
# 如果枚举左上角的话，就会出现需要判断右下角是否合理的情况，而且具有后效性了
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + grid[i - 1][j - 1]
        d = [[0] * (n + 2) for _ in range(m + 2)]
        for i2 in range(stampHeight, m + 1):
            for j2 in range(stampWidth, n + 1):
                i1 = i2 - stampHeight + 1
                j1 = j2 - stampWidth + 1
                if s[i2][j2] - s[i2][j1 - 1] - s[i1 - 1][j2] + s[i1 - 1][j1 - 1] == 0:
                    d[i1][j1] += 1
                    d[i2 + 1][j1] -= 1
                    d[i1][j2 + 1] -= 1
                    d[i2 + 1][j2 + 1] += 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                d[i][j] += d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1]
                if grid[i - 1][j - 1] == 0 and d[i][j] == 0:
                    return False
        return True
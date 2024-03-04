class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(land), len(land[0])
        #直接判断是否为矩形的左上角，然后遍历找到矩阵的右下角即可
        for i in range(m):
            for j in range(n):
                if land[i][j] and (not i or not land[i - 1][j]) and (not j or not land[i][j - 1]):
                    #当前肯定要为1，如果是第一行，并且前一列为空
                    #当前肯定要为1，如果是第一列，并且前一行为空
                    #当前肯定要为1，不是第一列或者第一行，左边和上边也是零
                    x, y = i, j
                    while x < m - 1 and land[x + 1][j]: x += 1
                    while y < n - 1 and land[i][y + 1]: y += 1
                    ans.append([i, j, x, y])
        return ans
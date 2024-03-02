class Solution:
    def minAreaFreeRect(self, p: List[List[int]]) -> float:
        eps = 1e-5
        n = len(p)
        # 找到一个点，然后求距离，得到最长的那个点是对角线，然后判断这两个点和附近两个点角度是不是九十度
        def dis(x1, y1, x2, y2):
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        def check(a, b, c, d):
            # 这种是全排列的情况，所以只要按着顺时针来搞就行了
            if((a[0] - d[0]) * (a[0] - b[0]) + (a[1] - d[1]) * (a[1] - b[1])) != 0 or ((c[0] - d[0]) * (c[0] - b[0]) + (c[1] - d[1]) * (c[1] - b[1])) != 0 or ((d[0] - a[0]) * (d[0] - c[0]) + (d[1] - a[1]) * (d[1] - c[1])) != 0:
                return inf
            return dis(a[0], a[1], b[0], b[1]) * dis(a[0], a[1], d[0], d[1])
        ans = inf
        # 暴力枚举所有的情况
        for i in range(n):
            for j in range(n):
                if i == j: continue
                for k in range(n):
                    if k == i or k == j: continue
                    if ((p[j][0] - p[i][0]) * (p[j][0] - p[k][0]) + (p[j][1] - p[i][1]) * (p[j][1] - p[k][1])) != 0: continue
                    for t in range(n):
                        if t == i or t == j or t == k: continue
                        ans = min(ans, check(p[i], p[j], p[k], p[t]))
        return ans if ans != inf else 0
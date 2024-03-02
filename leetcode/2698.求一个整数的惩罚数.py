class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = []
        t = []
        flag = None
        def dfs(i, x, y):
            n = len(x)
            nonlocal flag
            if i == n:
                tot = sum([int(c) for c in t])
                if tot == y:
                    flag = True
                return
            for j in range(i, n):
                t.append(x[i:j+1])
                dfs(j+1, x, y)
                t.pop()
        cnt = 0
        for i in range(1, n+1):        
            x = str(i * i)
            ans = []
            t = []
            flag = False
            dfs(0, x, i)
            if flag == True:
                cnt += i ** 2
        return cnt
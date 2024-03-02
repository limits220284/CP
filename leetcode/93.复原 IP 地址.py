class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        def check(ss):
            for c in ss:
                if c == '': return False
                if int(c) > 255: return False
                if len(c) >= 2 and c[0] == '0': return False
            return True
        path = []
        def dfs(start, cnt):
            if cnt == 0:
                if start == n and check(path):
                    ans.append(".".join(path))
                return
            for i in range(start, n):
                if i - start > 3: break
                path.append(s[start: i + 1])
                dfs(i + 1, cnt - 1)
                path.pop()
        dfs(0, 4)
        return ans
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 直接暴搜即可
        path = []
        vis = [False] * (1 << n)
        def dfs(num):
            vis[num] = True
            path.append(num)
            if len(path) == (1 << n):
                t = path[0] ^ path[-1]
                if bin(t).count('1') == 1:
                    return True
            for i in range(n):
                tp = num ^ (1 << i)
                if not vis[tp]:
                    if dfs(tp):
                        return True
            path.pop()
            vis[num] = False
            return False
        dfs(0)
        return path
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # 直接模拟
        vis = [False] * n
        p = list(range(n))
        vis[0] = True
        pre = 0
        t = 1
        while True:
            nxt = (pre + t * k) % n
            if not vis[nxt]:
                vis[nxt] = True
                pre = nxt
                t += 1
            else:
                break
        ans = []
        for i, x in enumerate(vis):
            if x == False:
                ans.append(i+1)
        return ans
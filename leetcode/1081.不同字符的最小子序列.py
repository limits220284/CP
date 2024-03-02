class Solution:
    # 直接构造的方法来写
    def smallestSubsequence1(self, s: str) -> str:
        st = sorted(list(set(s)))
        cidx = defaultdict(list)
        for i, c in enumerate(s):
            cidx[c].append(i)
        vis = [False] * len(st)
        cnt = 0
        i = -1
        ans = []
        while cnt < len(st):
            for j in range(len(st)):
                if vis[j]: continue
                notvis = [st[i] for i, x in enumerate(vis) if not vis[i]]
                idx1 = -1
                for k in cidx[st[j]]:
                    if k > i:
                        idx1 = k
                        break
                flag = True
                for c in notvis:
                    idxs = cidx[c]
                    if idxs[-1] < idx1:
                        flag = False
                        break
                if flag:
                    i = idx1
                    ans.append(st[j])
                    vis[j] = True
                    break
            cnt += 1
        return "".join(ans)
    # 全局来写
    def smallestSubsequence(self, s: str) -> str:
        left = Counter(s)
        ans = []
        vis = set()
        for c in s:
            left[c] -= 1
            if c in vis: continue
            while ans and ans[-1] > c and left[ans[-1]]:
                    vis.remove(ans.pop())
            ans.append(c)
            vis.add(c)
        return "".join(ans)
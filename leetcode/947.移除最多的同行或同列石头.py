class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        p = list(range(n))
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    a, b = find(i), find(j)
                    p[a] = b
        cnt = Counter()
        for x in p:
            a = find(x)
            cnt[a] += 1
        return n - len(cnt)
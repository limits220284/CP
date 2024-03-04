class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt = Counter()
        for x, y in zip(s1, s2):
            if x != y:
                cnt[x] += 1
        d = cnt['x'] + cnt['y']
        return -1 if d%2 else d//2 + cnt['x']%2
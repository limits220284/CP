class Solution:
    def countPairs(self, c: List[List[int]], k: int) -> int:
        cnt = Counter()
        ans = 0
        for x, y in c:
            for i in range(k+1):
                tx = x ^ i
                ty = y ^ (k - i)
                ans += cnt[(tx, ty)]
            cnt[(x, y)] += 1
        return ans
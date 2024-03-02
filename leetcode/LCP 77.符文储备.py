class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        n = len(runes)
        ans = cnt = 1
        for i in range(1, n):
            if runes[i] - runes[i-1] <= 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans
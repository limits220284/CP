class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # 双指针
        w = 0
        ans = n
        for r in range(n):
            if blocks[r] == 'W':
                w += 1
            if r >= k and blocks[r - k] == 'W':
                w -= 1
            if r >= k-1:
                ans = min(ans, w)
        return ans
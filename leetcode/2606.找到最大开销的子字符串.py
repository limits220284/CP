class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mapping = dict(zip(chars,vals))
        ans = f = 0
        # 空间优化dp
        for c in s:
            v = mapping.get(c, ord(c) - ord('a') + 1)
            f = max(f + v, v)
            ans = max(f, ans)
        return ans
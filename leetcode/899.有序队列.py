class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # 直接暴力求解
        # 采用sortedlist存放前k个的最小值，然后贪心的取出最大的
        if k >= 2:
            return "".join(sorted(list(s)))
        ans = s
        for i in range(len(s)):
            ans = min(ans, s[-i:] + s[:-i])
        return ans
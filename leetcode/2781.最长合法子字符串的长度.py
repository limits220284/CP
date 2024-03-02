class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # 双指针解法
        # 如果找到的字符串在forbidden内，
        n = len(word)
        st = set(forbidden)
        l = 0
        ans = 0
        for r in range(n):
            for j in range(r, max(r - 10, l-1), -1):
                if word[j: r+1] in st:
                    l = j + 1
                    break
            ans = max(ans, r - l + 1)
        return ans
        
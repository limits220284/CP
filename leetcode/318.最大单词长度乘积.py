class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 位运算进行优化
        n = len(words)
        bts = [0] * n
        for i, word in enumerate(words):
            t = 0
            for c in word:
                t |= 1 << (ord(c) - ord('a'))
            bts[i] = t
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bts[i] & bts[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
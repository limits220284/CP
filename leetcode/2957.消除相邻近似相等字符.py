class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # 贪心即可，每次都从中间修改
        word = [c for c in word]
        n = len(word)
        ans = 0 
        i = 1
        while i < n:
            if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
                ans += 1
                i += 2
            else:
                i += 1
        return ans
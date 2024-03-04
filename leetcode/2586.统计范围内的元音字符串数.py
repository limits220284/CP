class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        y = ['a','e','i','o','u']
        for i, word in enumerate(words):
            if word[0] in y and word[-1] in y and i<=right and i>=left:
                ans += 1
        return ans
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            word = word.split(separator)
            ans += word
        ans1 = []
        for c in ans:
            if c != "":
                ans1.append(c)
        return ans1
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        s = 0
        mx = 0
        ans1 = []
        for i, x in enumerate(groups):
            if x == s:
                mx += 1
                ans1.append(words[i])
                s = 1 - s
            else:
                continue
        s = 1
        mx = 0
        ans2 = []
        for i, x in enumerate(groups):
            if x == s:
                mx += 1
                ans2.append(words[i])
                s = 1 - s
            else:
                continue
        return ans1 if len(ans1) > len(ans2) else ans2
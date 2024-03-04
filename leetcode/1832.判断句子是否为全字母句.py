class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        exist = [False] * 26
        for c in sentence:
            exist[ord(c) - ord('a')] = True
        return all(exist)

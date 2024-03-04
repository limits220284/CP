class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        strs=sentence.strip().split()
        for i in range(len(strs)):
            ans=strs[i]
            if ans[:len(searchWord)]==searchWord:
                return i+1
        return -1

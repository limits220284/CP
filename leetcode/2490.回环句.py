class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr=list(sentence.strip().split())
        n=len(arr)
        for i in range(n-1):
            if arr[i][-1]!=arr[i+1][0]:
                return False
        if arr[-1][-1]!=arr[0][0]:
            return False
        return True
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n=len(words)
        cnt=0
        for i in range(n-1):
            for j in range(i+1,n):
                if set(words[i])==set(words[j]):
                    cnt+=1
        return cnt
                
                
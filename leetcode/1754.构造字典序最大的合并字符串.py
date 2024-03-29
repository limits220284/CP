class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n,m=len(word1),len(word2)
        i,j=0,0
        res=''
        while i<n and j<m:
            if word1[i]>word2[j]:
                res+=word1[i]
                i+=1
            elif word1[i]<word2[j]:
                res+=word2[j]
                j+=1
            else:
                if word1[i:]>word2[j:]:
                    res+=word1[i]
                    i+=1
                else:
                    res+=word2[j]
                    j+=1

        while i<n:
            res+=word1[i]
            i+=1
        while j<m:
            res+=word2[j]
            j+=1
        return res
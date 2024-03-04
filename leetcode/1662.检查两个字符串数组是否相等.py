class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # 遍历求解
        i,j=0,0
        l,r=0,0
        m,n=len(word1),len(word2)
        while l<m and r<n:
            x,y=len(word1[l]),len(word2[r])
            while i<x and j<y:
                if word1[l][i]!=word2[r][j]:
                    return False
                i+=1
                j+=1
            l+= 1 if i==x else 0
            i-= x if i==x else 0
            r+= 1 if j==y else 0
            j-= y if j==y else 0
        return i==0 and j==0 and l==m and r==n
                
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #字符串匹配即可
        n=len(s)
        m=len(t)
        i,j=0,0
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j==m:
            return 0
        return m-j
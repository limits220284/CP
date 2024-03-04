class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        # 如果前面的可以被整除,看当前的是否能够被整除
        n = len(word)
        ans = [0]*n
        tot = int(word[0])%m
        if tot==0:
            ans[0]=1
        for i in range(1,n):
            tot=tot*10+int(word[i])
            tot=tot%m
            if tot==0:
                ans[i]=1
        return ans
                    
                
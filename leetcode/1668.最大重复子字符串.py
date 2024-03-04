class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=len(word)
        n=len(sequence)
        l,r=0,n//k
        while l<r:
            mid=(l+r+1)//2
            ans="".join([word]*mid)
            if sequence.count(ans):
                l=mid
            else:
                r=mid-1
        return l
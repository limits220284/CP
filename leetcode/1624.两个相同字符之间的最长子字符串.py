class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic={}
        res=-1
        for i,x in enumerate(s):
            if x not in dic:
                dic[x]=i
            else:
                res=max(res,i-dic[x]-1)
        return res
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        n=len(s)
        def dfs(idx,st):
            if idx==n:
                res.append(''.join(st))
                return 
            if st[idx].isdigit():
                dfs(idx+1,st)
            else:
                dfs(idx+1,st)
                st[idx]=st[idx].swapcase()
                dfs(idx+1,st)
        dfs(0,[x for x in s])
        return res
        
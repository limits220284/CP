class Solution:
    def maxScore(self, nums: List[int]) -> int:
        #采用dfs应该怎么写
        n=len(nums)
        arr=[]
        gcd_value=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                gcd_value[i][j]=gcd(nums[i],nums[j])

        def cal(ans):
            cnt=0
            ans.sort()
            for i,x in enumerate(ans):
                cnt+=(i+1)*x
            return cnt
        res=0
        vis=[False]*n
        def dfs(be,k):
            nonlocal res
            if 2*k == n:
                res=max(res,cal(arr[::]))
                return
            # dfs出所有的组合即可
            inx=be
            while vis[inx]==True:
                inx+=1
            vis[inx]=True
            for i in range(inx+1,n):
                if not vis[i]:
                    vis[i]=True
                    arr.append(gcd_value[inx][i])
                    dfs(inx+1,k+1)
                    arr.pop()
                    vis[i]=False
            vis[inx]=False
        dfs(0,0)
        return res
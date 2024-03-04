# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        @cache
        def xhj(arr):
            N=int(1e5+10)
            cnt=0
            vis=[False]*N
            q=[0]*N
            n=len(arr)
            for i in range(1,n+1):
                q[arr[i-1]]=i
            ans=0
            for i in range(1,n+1):
                vis[arr[i-1]]=True
                np=q[arr[i-1]]
                cnt=1
                while q[np]!=np and vis[np]==False:
                    cnt+=1
                    vis[np]=True
                    np=q[np]
                ans+=cnt-1
            return ans
        
        que=deque()
        que.append(root)
        tot=0
        while que:
            n=len(que)
            res=[]
            for i in range(n):
                ans=que.popleft()
                res.append(ans.val)
                if ans.left:
                    que.append(ans.left)
                if ans.right:
                    que.append(ans.right)
            # 需要映射到(1,n)当中
            tp=sorted(res)
            tmp=[]
            dic={}
            for i,x in enumerate(tp):
                dic[x]=i+1
            for x in res:
                tmp.append(dic[x])
            tot+=xhj(tuple(tmp))
        return tot
            
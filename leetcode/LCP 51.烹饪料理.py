class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        n=len(cookbooks)
        self.ans=-1
        def dfs(idx,x,y):
            if idx==n:
                if y>=limit:
                    self.ans=max(self.ans,x)
                return
            # 选择制作该料理
            if all(cookbooks[idx][j]<=materials[j] for j in range(5)):
                for i in range(5):
                    materials[i]-=cookbooks[idx][i]
                dfs(idx+1,x+attribute[idx][0],y+attribute[idx][1])
                for i in range(5):
                    materials[i]+=cookbooks[idx][i]
            # 不制作该料理
            dfs(idx+1,x,y)
        dfs(0,0,0)
        return self.ans
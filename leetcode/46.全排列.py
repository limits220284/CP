class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        t = []
        n = len(nums)
        vis = [False] * n
        def dfs(i: int):
            if i == n:
                ans.append(t[::])
                return
            for j in range(n):
                if not vis[j]:
                    t.append(nums[j])
                    vis[j] = True
                    dfs(i+1)
                    vis[j] = False
                    t.pop() 
        dfs(0)
        return ans
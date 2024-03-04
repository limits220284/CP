class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        t = []
        vis = [False] * n
        def dfs():
            if len(t) == n:
                ans.append(t[::])
                return
            for j in range(n):
                if vis[j] or j and nums[j] == nums[j-1] and not vis[j-1]:
                    continue
                t.append(nums[j])
                vis[j] = True
                dfs()
                t.pop()
                vis[j] = False
        nums.sort()
        dfs()
        return ans
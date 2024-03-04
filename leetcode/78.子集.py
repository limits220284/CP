class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        t = []
        # 输出答案的视角
        def dfs(inx):
            ans.append(t[::])
            if inx == n:
                return
            for j in range(inx, n):
                t.append(nums[j])
                dfs(j+1)
                t.pop()
        dfs(0)
        return ans
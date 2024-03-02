class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        path = []
        def dfs(start, target):
            if target == 0:
                ans.append(list(path))
                return 
            for i in range(start, n):
                if target - candidates[i] < 0:
                    break
                path.append(candidates[i])
                dfs(i, target - candidates[i])
                path.pop()
        candidates.sort()
        dfs(0, target)
        return ans
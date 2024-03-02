class Solution:
    def combinationSum21(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        n = len(candidates)
        def dfs(start, target):
            if target == 0:
                ans.append(list(path))
                return
            # 从start开始是为了求组合
            for i in range(start, n):
                if target - candidates[i] < 0:
                    break
                # 这一部分是为了在同一层，如果上一个已经被选择过了，并且和上个一样，
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, target - candidates[i])
                path.pop()

        candidates.sort()
        dfs(0, target)
        return ans
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 背包问题
        f = [set() for _ in range(target + 1)]
        for c in sorted(candidates):
            if c > target:
                continue
            # 为什么背包模型不能够正序
            # 因为如果一旦正序，后面的结果就会利用前面已经更新完毕的结果
            for j in range(target, c-1, -1):
                if f[j-c]:
                    for item in f[j-c]:
                        f[j].add(item + (c,))
            f[c].add((c, ))
        return [list(x) for x in f[target]]
            
        
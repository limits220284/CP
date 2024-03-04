class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # # 选或者不选
        # ans = []
        # t = []
        # def dfs(i: int,target: int):
        #     if target == 0 and len(t) == k:
        #         ans.append(t[::])
        #         return
        #     if target < 0:
        #         return
        #     r = 10-i
        #     if r < k-len(t) or (i+9)*r//2 < target:
        #         return
        #     # 不选
        #     dfs(i+1, target)
        #     # 选
        #     t.append(i)
        #     dfs(i+1, target-i)
        #     t.pop()
        # dfs(1, n)
        # return ans
        ans = []
        t = []
        def dfs(i: int, target: int):
            if target < 0:
                return
            if target == 0 and len(t) == k:
                ans.append(t[::])
                return           
            r = 10-i
            if r < k-len(t) or (i+9)*r//2 < target:
                return
            for j in range(i, 10):
                t.append(j)
                dfs(j+1, target-j)
                t.pop()
        dfs(1, n)
        return ans
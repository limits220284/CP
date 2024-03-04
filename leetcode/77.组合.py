class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 这题没法用二进制枚举了
        # 1、选或者不选
        ans = []
        t = []
        def dfs(i: int):
            if len(t) == k:
                ans.append(t[::])
                return
            # 不选
            if k-len(t) > n-i+1:
                return
            dfs(i+1)
            # 选
            t.append(i)
            dfs(i+1)
            t.pop()
        dfs(1)
        return ans
        # 2、下一个选什么
        # ans = []
        # t = []
        # def dfs(i: int):
        #     # 如果剩余的数字都不够填满k的,则返回
        #     # 歪日这个减枝真尼玛绝了
        #     if k-len(t) > n-i+1:
        #         return
        #     if len(t) == k:
        #         ans.append(t[::])
        #         return
        #     for j in range(i, n+1):
        #         t.append(j)
        #         dfs(j+1)
        #         t.pop()           
        # dfs(1)
        # return ans
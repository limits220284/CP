class Solution:
    def kthSmallest1(self, mat: List[List[int]], k: int) -> int:
        # 暴力搜索n ^ m次方，可以写一个暴力解法，然后取前k个
        # 但是k只有200个
        # 采用堆来进行寻找结果
        def prod(arr):
            res = 1
            for x in arr:
                res *= x
            return res
        m, n = len(mat), len(mat[0])
        arr = []
        for i, ma in enumerate(mat):
            for x in ma:
                arr.append((x, i))
        print(arr)
        arr.sort()
        print(arr)
        row = [0] * m
        tmp = [[] for _ in range(m)]
        wei = 0
        for val, i in arr:
            tmp[i].append(val)
            row[i] += 1
            if prod(row) > k:
                wei = val
                break
        # 如果当前加入的数字后面还有重复的，就把后面重复的都加入进来
        cur = sum(row)
        while cur < m * n and arr[cur][0] == wei:
            val, i = arr[cur]
            tmp[i].append(val)
            cur += 1
        ans = []
        print(tmp)
        # 写一个回溯计算所有的结果
        def dfs(i, cnt):
            if i == len(tmp):
                ans.append(cnt)
                return
            for x in tmp[i]:
                dfs(i + 1, cnt + x)
        dfs(0, 0)
        print(ans)
        ans.sort()
        print(ans)
        return ans[k - 1]
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        a = mat[0][:k]
        for row in mat[1:]:
            a = sorted(x + y for x in a for y in row)[:k]
        return a[-1]











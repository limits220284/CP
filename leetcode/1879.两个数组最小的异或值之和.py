class Solution:
    def minimumXORSum1(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        alls = []
        path = []
        vis = [False] * n
        def dfs():
            if len(path) == n:
                alls.append(copy.copy(path))
                return
            for i in range(n):
                if vis[i]: continue
                path.append(nums2[i])
                vis[i] = True
                dfs()
                vis[i] = False
                path.pop()
        dfs()
        ans = inf
        for nums in alls:
            tmp = 0
            for x, y in zip(nums, nums1):
                tmp += x ^ y
            ans = min(ans, tmp)
        return ans
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        f = [inf] * (1 << n)
        f[0] = 0
        for mask in range(1, 1 << n):
            c = bin(mask).count("1")
            for i in range(n):
                if mask >> i & 1:
                    f[mask] = min(f[mask], f[mask ^ (1 << i)] + (nums2[c - 1] ^ nums1[i]))
        return f[(1 << n) - 1]
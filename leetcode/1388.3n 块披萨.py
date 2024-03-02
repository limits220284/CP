class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # 问题从3N个数中选择n个数的最大值
        # f[i][j]表示从前i个数中选择j个数的最大值
        # f[i][j] = max(f[i-1][j], f[i-2][j-1] + arr[i])
        def work(arr):
            n = len(arr)
            tar = (len(arr) + 1) // 3
            f = [[0] * (tar + 1) for _ in range(n+1)]
            f[1][1] = arr[0]
            for i in range(2, n+1):
                for j in range(1, tar+1):
                    f[i][j] = max(f[i-1][j], f[i-2][j-1] + arr[i-1])
            return f[n][tar]
        return max(work(slices[1:]), work(slices[:-1]))
        


        
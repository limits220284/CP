#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        f = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                f[i][j] = max(f[i-1][j], f[i][j-1])
                if a[i-1] == b[j-1]: f[i][j] = max(f[i][j], f[i-1][j-1] + 1)
        tot = f[m][n]
        arr = []
        i, j = m, n
        while i >= 0 and j >= 0:
            if tot == 0: break
            if a[i-1] == b[j-1]:
                arr.append(a[i-1])
                i -= 1; j -= 1; tot -= 1
            else:
                if f[i-1][j] == tot: i -= 1
                elif f[i][j-1] == tot: j -= 1
        arr = arr[::-1]
        i, j, k = 0, 0, 0
        ans = []
        while k < len(arr):
            while a[i] != arr[k]:
                ans.append(a[i])
                i += 1
            while b[j] != arr[k]:
                ans.append(b[j])
                j += 1
            ans.append(arr[k])
            k += 1; i += 1; j += 1
        while i < m:
            ans.append(a[i])
            i += 1
        while j < n:
            ans.append(b[j])
            j += 1
        return "".join(ans)


#
# @lc app=leetcode.cn id=1943 lang=python3
#
# [1943] 描述绘画结果
#

# @lc code=start
class Solution:
    def splitPainting1(self, segments: List[List[int]]) -> List[List[int]]:
        n = max(r for _, r, _ in segments)
        arr = [0] * (n+2)
        vis = [False] * (n+1)
        for l, r, c in segments:
            arr[l] += c
            arr[r] -= c
            vis[l] = vis[r] = True
        ans = []
        for i in range(1, n+1):
            arr[i] += arr[i-1]
        pre = -1
        for i in range(1, n+1):
            if vis[i] and pre != -1:
                if arr[pre] != 0:
                    ans.append([pre, i, arr[pre]])
                pre = i
            elif vis[i]:
                pre = i
        return ans
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # 只和端点有关，也就是端点的加和减
        d = defaultdict(int)
        for a, b, val in segments:
            d[a] += val
            d[b] -= val
        q = []
        cur = 0
        pre = -1
        for p in sorted(d.keys()):
            if pre != -1 and cur:
                q.append([pre, p, cur])
            cur += d[p]
            pre = p
        return q
    
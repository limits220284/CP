#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
#

# @lc code=start
class Solution:
    def eventualSafeNodes1(self, graph: List[List[int]]) -> List[int]:
        # 只要能够形成环，就不算安全节点，
        # 先找到图中所有的环经过的节点，将这些节点排除
        n = len(graph)
        vis = [False] * n
        # 先建图, 去除自环的点，然后将该点加入非安全序列中
        _NOT = []
        g = [[] for _ in range(n)]
        for i, arr in enumerate(graph):
            for x in arr:
                if x == i:
                    _NOT.append(i)
                    continue
                g[i].append(x)
        # 怎么将其变成找环的题目？

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 反向建图，反向拓扑序列
        # 如果不能够建立拓扑序列，那么剩余的就是环
        n = len(graph)
        _IN = [0] * n
        g = [[] for _ in range(n)]
        for i, arr in enumerate(graph):
            for x in arr:
                g[x].append(i)
                _IN[i] += 1
        ans = []
        q = deque(i for i, d in enumerate(_IN) if d == 0)
        while q:
            x = q.popleft()
            ans.append(x)
            for y in g[x]:
                _IN[y] -= 1
                if _IN[y] == 0:
                    q.append(y)
        ans.sort()
        return ans

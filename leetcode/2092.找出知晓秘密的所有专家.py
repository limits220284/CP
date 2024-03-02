#
# @lc app=leetcode.cn id=2092 lang=python3
#
# [2092] 找出知晓秘密的所有专家
#

# @lc code=start

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # 分时间dfs
        known = set([0, firstPerson])
        meetings.sort(key = lambda x: x[2])
        print(meetings)
        n = len(meetings)
        i = 0
        while i < n:
            time = meetings[i][2]
            # 建立图，采用hash表建图
            g = defaultdict(list)
            g_known = set()
            while i < n and meetings[i][2] == time:
                g[meetings[i][0]].append(meetings[i][1])
                g[meetings[i][1]].append(meetings[i][0])
                if meetings[i][0] in known:
                    g_known.add(meetings[i][0])
                if meetings[i][1] in known:
                    g_known.add(meetings[i][1])
                i += 1
            # print(time, g)
            # 遍历图，从g_know中选点
            vis = {}
            def dfs(x):
                vis[x] = True
                for y in g[x]:
                    if y not in vis:
                        known.add(y)
                        dfs(y)
            for x in g_known:
                dfs(x)
            # print(g_known)
        return list(known) 

#
# @lc app=leetcode.cn id=1882 lang=python3
#
# [1882] 使用服务器处理任务
#

# @lc code=start
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # 遍历每一个任务，tasks中的下标是开始的时间，tasks[i]是任务所需要持续的时间
        # 因为每次都需要权重最小的服务器，所以需要维护两个堆，一个是正在使用的，一个是还未被占用的
        # [31,96,73,90,15,11,1,90,72,9,30,88]
        # [87,10,3,5,76,74,38,64,16,64,93,95,60,79,54,26,30,44,64,71]
        h_not = []
        h_is = []
        # 权重作为第一性，如果权重相同，下标最小的先弹出
        for i, wt in enumerate(servers): heappush(h_not, (wt, i))
        n = len(tasks)
        ans = [0] * n
        cur_time = 0
        for i, task in enumerate(tasks):
            # 遍历tasks
            # 如果当前时间大于占用服务器的时间，服务器出来
            cur_time = max(cur_time, i)
            while h_is and i >= h_is[0][0]:
                server = heappop(h_is)
                heappush(h_not, server[1])
            if not h_not:
                time = h_is[0][0]
                cur_time = max(cur_time, time)
                while h_is and time >= h_is[0][0]:
                    server = heappop(h_is)
                    heappush(h_not, server[1])
            server = heappop(h_not)
            heappush(h_is, (cur_time + task, server))
            ans[i] = server[1]
        return ans

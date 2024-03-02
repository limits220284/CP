#
# @lc app=leetcode.cn id=1986 lang=python3
#
# [1986] 完成任务的最少工作时间段
#

# @lc code=start
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # 二分+回溯
        # 二分是用来确定最少的工作时间段
        n = len(tasks)
        l, r = 1, n
        def check(mid):
            # mid 是桶的个数
            # 回溯判断这些桶是否能够装满
            arr = [sessionTime] * mid
            def dfs(i):
                if i == n:
                    return True
                # 当前桶是否能够继续装
                for j in range(mid):
                    if j > 0 and arr[j] == arr[j-1]:
                        continue
                    if arr[j] >= tasks[i]:
                        arr[j] -= tasks[i]
                        if dfs(i+1):
                            return True
                        arr[j] += tasks[i]
                return False
            return dfs(0)
        tasks.sort(reverse = True)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l



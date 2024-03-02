class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        flag = False
        for interval in intervals:
            if newInterval[0] > interval[1]:
                ans.append(interval)
            elif newInterval[1] >= interval[0] and interval[1] >= newInterval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            elif interval[0] > newInterval[1]:
                if not flag:
                    ans.append(newInterval)
                    flag = True
                ans.append(interval)
        if not flag:
            ans.append(newInterval)
        return ans
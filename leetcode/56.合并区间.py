class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # 按着左端点升序排序
        intervals.sort(key = lambda x: x[0])
        ans = []
        for interval in intervals:
            if not ans:
                ans.append(interval)
            else:
                if interval[0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], interval[1])
                else:
                    ans.append(interval)
        return ans
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for i, j in tasks:
            ans += i
            if ans < j:
                ans = j
        return ans

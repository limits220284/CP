class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for x in hours:
            if x >= target:
                ans += 1
        return ans
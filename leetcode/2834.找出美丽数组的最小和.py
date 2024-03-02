class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        vis, ans, p, cnt = set(), 0, 1, 0
        while cnt < n:
            if p not in vis:
                ans += p
                if target - p > 0:
                    vis.add(target - p)
                p+=1
                cnt += 1
            else:
                p+=1
        return ans
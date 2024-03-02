class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(mid):
            for i in range(k):
                tot = 0
                arr = [mid * composition[i][j] for j in range(n)]
                for j, x in enumerate(arr):
                    tot += (max(0, x - stock[j])) * cost[j]
                if tot <= budget:
                    return True
            return False
        l, r = 0, min(stock) + budget
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
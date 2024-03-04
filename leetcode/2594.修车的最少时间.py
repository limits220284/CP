class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # 二分答案
        def check(mid):
            mx = 0
            for rank in ranks:
                mx += int(math.sqrt(mid//rank))
            return mx >= cars
        l, r = 0, 10**17
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
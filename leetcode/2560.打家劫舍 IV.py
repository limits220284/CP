class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # solve(mx) 返回最大金额为 mx 时，最多可以偷多少间房子
        def solve(mx: int) -> int:
            f0 = f1 = 0
            for x in nums:
                if x > mx:
                    f0 = f1
                else:
                    f0, f1 = f1, max(f1, f0 + 1)
            return f1
        return bisect_left(range(max(nums)), k, key=solve)

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n=len(nums)
        s = set()
        ans = 0
        for x in nums:
            s.add(x)
            if x - diff in s and x - 2*diff in s:
                ans += 1
        return ans
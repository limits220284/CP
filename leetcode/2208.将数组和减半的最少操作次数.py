class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # 永远减去最大的准没错
        n = len(nums)
        tot = 0
        limit = sum(nums) / 2
        h = []
        for x in nums: heappush(h, -x)
        ans = 0
        while tot < limit:
            x = heappop(h) / 2
            tot -= x
            heappush(h, x)
            ans += 1
        return ans
        

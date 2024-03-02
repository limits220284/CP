"""
枚举所有nums[i] & nums[j] 的个数，采用hash表进行统计
然后遍历k，如果 & 为零，则直接统计个数

"""
class Solution:
    def countTriplets1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = Counter(x & y for x in nums for y in nums)
        for x in nums:
            for ky, val in cnt.items():
                if x & ky == 0:
                    ans += val
        return ans
    def countTriplets(self, nums: List[int]) -> int:
        cnt = [0] * (1 << 16)
        for x in nums:
            for y in nums:
                cnt[x & y] += 1
        ans = 0
        for m in nums:
            m ^= 0xffff
            ans += cnt[m]
            s = m
            while s:
                s = (s - 1) & m
                ans += cnt[s]
        return ans
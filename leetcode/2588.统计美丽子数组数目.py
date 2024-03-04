class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        dic = {0:1}
        pre = 0
        ans = 0
        for x in nums:
            pre ^= x
            if pre in dic:
                ans += dic[pre]
                dic[pre] += 1
            else:
                if pre == 0:
                    ans += 1
                dic[pre] = 1
        return ans
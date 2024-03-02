class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        for x in nums:
            i = 0
            while x:
                if x & 1:
                    bits[i] += 1
                x >>= 1
                i += 1
        i = 0
        ans = 0
        for i in range(len(bits)):
            if bits[i] >= k:
                ans += 2 ** i
        return ans
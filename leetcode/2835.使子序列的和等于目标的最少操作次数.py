class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        h = defaultdict(int)
        nums.sort()
        for num in nums:
            h[num]+=1
        ans, p = 0, 0
        while target != 0:
            c = target % 2
            target //= 2
            n = 2 ** p
            if c == 0:
                if h[n] >= 2:
                    h[n*2] += h[n] // 2
                    h[n] %= 2
                p += 1
                continue
            if h[2**p]>0:
                h[2**p]-=1
            else:
                i = p + 1
                while h[2 ** i] == 0:
                    h[2**i] = 1
                    i += 1
                ans += (i-p)
                h[2**i] -= 1
            p += 1
            if h[n] >= 2:
                h[n*2] += h[n] // 2
                h[n] %= 2
        return ans
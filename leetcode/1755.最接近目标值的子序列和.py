class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # 如果直接二进制枚举，会导致乘以一个n的复杂度，现在采用状态压缩进行优化
        def work(arr):
            m = len(arr)
            f = [0] * (1 << m)
            for i in range(1, 1 << m):
                f[i] = f[i^i&-i] + arr[(i&-i).bit_length()-1]
            return sorted(list(set(f)))
        n = len(nums)
        m = n // 2
        A, B = work(nums[:m]), work(nums[m:])
        ans = inf
        for b in B:
            l, r = 0, len(A)-1
            while l < r:
                mid = (l + r) // 2
                if A[mid] + b - goal >= 0:
                    r = mid
                else:
                    l = mid + 1
            if l > 0: ans = min(ans, abs(A[l-1] + b - goal))
            ans = min(ans, abs(A[l] + b - goal))
            if ans == 0: break
        return ans
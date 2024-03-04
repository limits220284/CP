class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        p = [q - i for i, q in enumerate(i for i, x in enumerate(nums) if x)]
        s = list(accumulate(p, initial=0))  # p 的前缀和
        return min(s[i] + s[i + k] - s[i + k // 2] * 2 - p[i + k // 2] * (k % 2)
                   for i in range(len(p) - k + 1))  # p[i:i+k] 中所有数到 p[i+k//2] 的距离之和，取最小值
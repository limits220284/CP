"""
可以想到的是如果相等，删除偶数位或者奇数位，效果都是一样的
那么就直接遍历，如果遇到相同的直接删除，删除奇数位，把指针下移，直到出现不同的数字
然后将指针都加1继续下一轮的删除即可
"""
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return n
        l, r = 0, 1
        cnt = 0
        while r < n:
            if nums[l] == nums[r]:
                r += 1
                cnt += 1
            else:
                l = r + 1
                r += 2
        if (n - cnt) % 2:
            cnt += 1
        return cnt
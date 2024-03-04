class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mex = 0
        cnt = Counter(x % value for x in nums)
        while cnt[mex%value]:
            cnt[mex%value] -= 1
            mex += 1
        return mex 
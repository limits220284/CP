class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        def check(k):
            # 判断是否存在k对
            cnt = 0
            for i in range(k):
                if 2*nums[i] <= nums[n-k+i]:
                    cnt += 1
            return cnt >= k


        l, r =0,n//2
        while l < r:
            mid = (l+r+1)//2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l*2

        
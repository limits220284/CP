class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.num=[0 for i in range(n+1)]
        for i in range(1,n+1):
            self.num[i]=self.num[i-1]+nums[i-1]
        print(self.num)
            

    def sumRange(self, left: int, right: int) -> int:
        return self.num[right+1]-self.num[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
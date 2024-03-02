class NumArray:
    def lowbit(self, x):
        return x & -x # 利用负数的补码
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tr = [0] * (self.n + 1)
        for i, x in enumerate(nums):
            self.insert(i, x)
    def insert(self, i, val):
        i += 1
        while i <= self.n:
            self.tr[i] += val
            i += self.lowbit(i)
    def update(self, index: int, val: int) -> None:
        t = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= self.n:
            self.tr[index] += t
            index += self.lowbit(index)
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tr[idx]
            idx -= self.lowbit(idx)
        return res
    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 对于3和30来说,应该是30排放到前面
        def compare(x, y):
            if y+x >= x+y:
                return 1
            else:
                return -1
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        print(nums)
        return "0" if nums[0]=="0" else "".join(nums)
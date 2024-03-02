class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0
        # 拆位计算
        highbit = max(nums).bit_length() - 1
        for i in range(highbit, -1, -1):
            mask |= 1 << i
            new_ans = ans | (1 << i)
            vis = set()
            for x in nums:
                new_x = x & mask
                if new_x ^ new_ans in vis:
                    ans = new_ans
                    break
                vis.add(new_x)
        return ans

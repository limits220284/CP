class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 先维护一下数组中的递减序列
        n = len(nums)
        stk = []
        for num in reversed(nums):
            while stk and num >= stk[-1]:
                stk.pop()
            stk.append(num)
        print(stk)
        ans = []
        for num in reversed(nums):
            while stk and num >= stk[-1]:
                stk.pop()
            ans.append(-1 if not stk else stk[-1])
            stk.append(num)
        return list(reversed(ans))
class Solution:
    def secondGreaterElement1(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        s = []
        t = []
        ans = [-1] * len(nums)
        for i, x in enumerate(nums):
            while t and x > nums[t[-1]]:
                ans[t[-1]] = x
                t.pop()
            j = len(s) - 1
            while j >= 0 and nums[s[j]] < x:
                j -= 1
            t += s[j + 1: ]
            del s[j + 1:]
            s.append(i)
        return ans
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        q = []
        for i in range(len(nums)):
            while len(q) and q[0][0] < nums[i]:
                ans[q[0][1]] = nums[i]
                heappop(q)
            while len(stack) and nums[stack[-1]] < nums[i]:
                heappush(q, (nums[stack[-1]], stack[-1]))
                stack.pop()
            stack.append(i)
        return ans
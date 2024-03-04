class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        stack=[]
        for a in arr:
            if not stack or stack[-1]<=a:
                stack.append(a)
            else:
                mx=stack.pop()
                while stack and stack[-1]>a:
                    stack.pop()
                stack.append(mx)
        return len(stack)
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, x in enumerate(variables):
            a, b, c, m = x
            if pow(pow(a, b, 10), c, m) == target:
                ans.append(i)
        return ans
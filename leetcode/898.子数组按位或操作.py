"""
或的结果只能增大
"""
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        tmp = set()
        for x in arr:
            tmp = {x | y for y in tmp}
            tmp.add(x)
            ans |= tmp
        return len(ans)
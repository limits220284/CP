class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            return "".join(['a' for i in range(n-1)])+'b'
        return "".join(['a' for i in range(n)])
        
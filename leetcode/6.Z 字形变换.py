class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        n = len(s)
        arr = [[] for _ in range(numRows)]
        for i in range(n):
            t = i % (numRows + numRows - 2)
            if t < numRows:
                arr[t].append(s[i])
            else:
                arr[numRows + numRows - 2 - t].append(s[i])
        return "".join(["".join(x) for x in arr])
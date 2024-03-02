class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans = []
        for i in range(1, k//2 + 1):
            ans.append(i)
        if len(ans) >= n:
            return sum(ans[:n])
        dis = n - len(ans)
        for x in range(k, k+dis):
            ans.append(x)
        return sum(ans)
            
        
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = [start]
        for i in range(n):
            for j in range(len(ans) - 1, -1, -1):
                ans.append((ans[j] ^ start | 1 << i) ^ start)
        return ans

        
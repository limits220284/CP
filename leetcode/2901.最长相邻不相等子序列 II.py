class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def ok(s: str, t: str) -> bool:
            return len(s) == len(t) and sum(x != y for x, y in zip(s, t)) == 1

        f = [0] * n
        from_idx = [0] * n
        mx = n - 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if f[j] > f[i] and groups[j] != groups[i] and ok(words[i], words[j]):
                    f[i] = f[j]
                    from_idx[i] = j
            f[i] += 1  # 加一写在这里
            if f[i] > f[mx]:
                mx = i

        ans = [''] * f[mx]
        for i in range(f[mx]):
            ans[i] = words[mx]
            mx = from_idx[mx]
        return ans

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        def work(x):
            lis = []
            for i in range(m):
                lis.append(x % 3)
                x //= 3
            return list(reversed(lis))
        valid = set()
        for state in range(3 ** m):
            lis = work(state)
            if any(lis[i] == lis[i + 1] for i in range(m - 1)):
                continue
            valid.add(state)
        adj = defaultdict(list)
        for state1 in valid:
            for state2 in valid:
                lis1, lis2 = work(state1), work(state2)
                if any(x == y for x, y in zip(lis1, lis2)):
                    continue
                adj[state1].append(state2)
        f = [[0] * (3 ** m) for _ in range(n)]
        f[0] = [int(state in valid) for state in range(3 ** m)]
        for i in range(1, n):
            for j in range(3 ** m):
                for val in adj[j]:
                    f[i][j] = (f[i][j] + f[i - 1][val]) % mod
        return sum(f[-1]) % mod
            
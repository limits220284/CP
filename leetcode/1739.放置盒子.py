f = [0] * 2000
for i in range(1, 2000):
    f[i] = f[i - 1] + (i + 1) * i // 2
# print(f)
g = [0] * 200000
for i in range(1, 200000):
    g[i] = i * (i + 1) // 2
# print(g)
class Solution:
    def minimumBoxes(self, n: int) -> int:
        ans = 0
        idx1 = bisect_right(f, n) - 1
        print(f[idx1], idx1)
        ans += idx1 * (idx1 + 1) // 2
        print(ans)
        idx2 = bisect_left(g, n - f[idx1])
        print(idx2)
        ans += idx2
        print(ans)
        return ans
        
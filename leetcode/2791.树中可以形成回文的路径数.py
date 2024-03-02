class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        # 树上的路径可以转换成二进制数，每往下遍历一次就在数字上加一位
        # 加的过程使用xor，当然减的过程也采用xor
        # 什么时候是答案呢？当a xor b == 0 or a xor b == 1 << i
        # 采用dfs进行树的遍历，遍历到一个点，就查找cnt中是否有使其成功的
        ans = 0
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            bit = ord(s[i]) - ord('a')
            g[parent[i]].append((i, 1 << bit))
        cnt = Counter()
        def dfs(x, xor):
            nonlocal ans
            ans += cnt[xor]
            for i in range(26):
                ans += cnt[xor ^ (1 << i)]
            cnt[xor] += 1
            for y, w in g[x]:
                dfs(y, w ^ xor)
        dfs(0, 0)
        return ans
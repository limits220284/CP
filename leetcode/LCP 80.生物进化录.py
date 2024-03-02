"""
遇到树的问题一般都要想到子问题
因为树是一个天然的递归结构
比如说该问题就可以转换成一个递归问题
对于一个节点,要想遍历完,保证字典序最小,首先需要保证遍历子树的顺序问题
可以转换成按着每一个子树遍历完后,再按着子树字典序从小到大的顺序遍历
这样可以保证字典序最小

"""
class Solution:
    def evolutionaryRecord(self, parents: List[int]) -> str:
        n = len(parents)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parents[i]].append(i)
        def dfs(x):
            if len(g[x]) == 0:
                return "01"
            a = sorted(dfs(y) for y in g[x])
            # print(a)
            return "0" + ''.join(a) + "1"
        ans = dfs(0)
        return ans[1:].rstrip('1')
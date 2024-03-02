"""
倍增
f[p][i]表示当前节点的2**i父节点是什么
f[p][0]表示自己的父节点 p'
f[p][1]表示自己的爷爷节点f[p][1] = f[p'][0]
f[p][i+1] = f[f[p][i]]][i]  
"""
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        BIT_LENGTH = n.bit_length() + 1
        f = [[-1] * BIT_LENGTH for _ in range(n)]
        for i in range(n): f[i][0] = parent[i]
        for i in range(1, BIT_LENGTH):
            for j in range(n):
                if f[j][i - 1] == -1: continue # 如果已经是不存在的了，就直接作为-1即可
                f[j][i] = f[f[j][i - 1]][i - 1]
        self.f = f
        # print(f)
    def getKthAncestor(self, node: int, k: int) -> int:
        # 采用lowbit快速计算最后一位
        # 6: 110
        while k:
            lb = k & -k
            k -= lb
            node = self.f[node][lb.bit_length() - 1]
            if node == -1:
                break
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
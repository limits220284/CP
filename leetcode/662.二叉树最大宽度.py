class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelMin = {}
        def dfs(node: Optional[TreeNode], depth: int, index: int) -> int:
            if node is None:
                return 0
            if depth not in levelMin:
                levelMin[depth] = index  # 每一层最先访问到的节点会是最左边的节点，即每一层编号的最小值
            return max(index - levelMin[depth] + 1,
                       dfs(node.left, depth + 1, index * 2),
                       dfs(node.right, depth + 1, index * 2 + 1))
        return dfs(root, 1, 1)
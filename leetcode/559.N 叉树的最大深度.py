"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            mx=0
            if not root:
                return 0
            for r in root.children:
                mx=max(mx,dfs(r))
            return mx+1
        return dfs(root)
        
        
        
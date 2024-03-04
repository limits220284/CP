# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                res.append('null')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        res=[]
        dfs(root)
        return '['+','.join(res)+']'
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data=='[]':
            return None
        ans=data[1:-1].split(',')
        root=TreeNode(ans[0])
        def dfs(root):
            nonlocal i
            if i==len(ans):
                return None
            if ans[i]=='null':
                root.left=None
            else:
                left=TreeNode(ans[i])
                i+=1
                root.left=dfs(left)
            i+=1
            if ans[i]=='null':
                root.right=None
            else:
                right=TreeNode(ans[i])
                i+=1
                root.right=dfs(right)
            return root
        i=1
        return dfs(root)           
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
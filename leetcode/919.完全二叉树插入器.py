# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root=root
        #统计数字数量
        def dfs(root):
            if not root:
                return 0                  
            return dfs(root.left)+dfs(root.right)+1
        self.cnt=dfs(root)
        

    def insert(self, val: int) -> int:
        self.cnt+=1
        n=self.cnt
        way=[]
        root=self.root
        highbit=n.bit_length()
        for i in range(highbit-2,0,-1):
            if n&(1<<i):
                root=root.right
            else:
                root=root.left
        ans=TreeNode(val)
        if n&1:
            root.right=ans
        else:
            root.left=ans
        return root.val
                
    def get_root(self) -> TreeNode:
        return self.root



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
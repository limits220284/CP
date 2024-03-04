class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        #序列化+hash存储
        def dfs(root):
            if not root:
                return ""
            serial="".join([str(root.val),'(',dfs(root.left),')(',dfs(root.right),')'])
            print(serial)
            if serial in dic:
                res.add(dic[serial])
            else:
                dic[serial]=root
            return serial
        dic=dict()
        res=set()
        dfs(root)
        return list(res)
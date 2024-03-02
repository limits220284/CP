# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 树形dp
        # 考虑当前节点的三种状态
        # 被父节点监控
        # 被子节点监控
        # 被自己监控
        # 所以需要计算这三种情况分别需要多少个摄像头
        # 1、本身就是摄像头，那么子节点可以是被父节点监控的节点或者本身就是摄像头
        # 2、父节点是摄像头，子节点可以是摄像头点或者被子节点监控的点
        # 3、子节点有一个摄像头，子节点是摄像头点或者被子摄像头点监视的点
        # 什么情况下能够取到全是mbc的情况呢？那只有mbc 全部小于 mbs，那么我们可以计算差值的最小值即可
        def dfs(node):
            if not node:
                return inf, 0, 0
            lmbs, lmbf, lmbc = dfs(node.left)
            rmbs, rmbf, rmbc = dfs(node.right)
            mbs = min(lmbs, lmbf, lmbc) + min(rmbs, rmbf, rmbc) + 1
            mbf = min(lmbs, lmbc) + min(rmbs, rmbc)
            mbc = mbf + max(0, min(lmbs - lmbc, rmbs - rmbc))
            # 
            return mbs, mbf, mbc
        mbs, mbf, mbc = dfs(root)
        return min(mbs, mbc)
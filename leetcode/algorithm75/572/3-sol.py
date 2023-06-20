# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def dfs(node,node2):
            if not node and not node2:
                return True
            elif not node:
                return False
            elif not node2:
                return False
            else:
                a = False
                if node.val == node2.val:
                    a = dfs(node.left,node2.left) and dfs(node.right,node2.right) 
                if node2.val != subRoot.val:
                    node2 = subRoot
                return a or dfs(node.left,node2) or dfs(node.right,node2)

        
        return dfs(root,subRoot)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
MINVAL = -2**31 -1
MAXVAL = 2**31
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node, lo, hi):
            if node is None:
                return True
            return (lo < node.val < hi) and check(node.left, lo, node.val) and check(node.right, node.val, hi)
        return check(root, MINVAL, MAXVAL)
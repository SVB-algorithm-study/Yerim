# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ans = []
        def f(lv, node):
            if len(ans)-1 < lv:
                ans.append([node.val])
            else:
                ans[lv].append(node.val)
            for child in [node.left, node.right]:
                if child != None:
                    f(lv+1, child)
        f(0, root)
        return ans
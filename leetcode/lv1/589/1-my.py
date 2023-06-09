"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        def dfs(node):
            ans.append(node.val)
            for child in node.children:
                dfs(child)

        if root:
            dfs(root)

        return ans
        
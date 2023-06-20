import collections
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
        if root is None:
            return []
        
        result = []
        q = deque([root])
        while q:
            num_nodes = len(q)
            temp = []
            for _ in range(num_nodes):
                node = q.pop()
                temp.append(node.val)
                if node.left is not None:
                    q.appendleft(node.left)
                if node.right is not None:
                    q.appendleft(node.right)
            result.append(temp)
        return result
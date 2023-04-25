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
        def findRoot(node):
            if not node:
                return None
            if node.val == subRoot.val:
                return node
            left = findRoot(node.left)
            right = findRoot(node.right)
            if left:
                return left
            elif right:
                return right
            else:
                return None
        
        oriNode = findRoot(root)
        if not oriNode:
            return False

        oriq = collections.deque([oriNode])
        subq = collections.deque([subRoot])
        while oriq:
            o = oriq.popleft()
            s = subq.popleft()
            if not o and not s:
                continue
            elif not o or not s:
                return False
            if o.val != s.val:
                assert(0)
                return False  
            if o:          
                oriq.append(o.left)
                oriq.append(o.right)
            if s:
                subq.append(s.left)
                subq.append(s.right)
        return True
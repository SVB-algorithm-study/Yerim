"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        clonedict = {node.val: Node(node.val, [])}
        q = deque([node])
        while q:
            curnode = q.popleft()
            curclone = clonedict[curnode.val]
            for nextnode in curnode.neighbors:
                if not clonedict.get(nextnode.val, False):
                    clonedict[nextnode.val] = Node(nextnode.val, [])
                    q.append(nextnode)
                curclone.neighbors.append(clonedict[nextnode.val])
        return clonedict[node.val]
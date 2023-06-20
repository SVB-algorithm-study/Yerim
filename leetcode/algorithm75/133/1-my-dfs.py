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
        visited = [None]*101
        newnode = Node(node.val, [])
        def dfs(node, curnode):
            visited[node.val] = curnode
            for nextnode in node.neighbors:
                nextnewnode = visited[nextnode.val]
                if not nextnewnode:
                    nextnewnode = Node(nextnode.val, [])
                    dfs(nextnode, nextnewnode)
                curnode.neighbors.append(nextnewnode)
        dfs(node, newnode)
        return newnode
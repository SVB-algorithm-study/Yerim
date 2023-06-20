# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prevlist = set()
        node = head
        while node:
            if node in prevlist:
                return node
            prevlist.add(node)
            node = node.next
        return None
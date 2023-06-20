# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodelist = []
        node = head
        while node:
            nodelist.append(node)
            node = node.next
        return nodelist[len(nodelist)//2]
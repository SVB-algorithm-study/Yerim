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
        l = 0
        while node:
            nodelist.append(node)
            node = node.next
            l += 1
        for i in range(l//2):
            head = head.next
        return head
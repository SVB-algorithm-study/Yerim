# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mergesort = ms = ListNode(-1)
        
        while list1 and list2:
            if list1.val < list2.val:
                ms.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                ms.next = ListNode(list2.val, None)
                list2 = list2.next
            ms = ms.next
            
        ms.next = list1 if not list2 else list2

        return mergesort.next
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
        if not list1:
            return list2
        elif not list2:
            return list1

        mergesort = ms = None
        if list1.val < list2.val:
            mergesort = ms = ListNode(list1.val, None)
            list1 = list1.next
        else:
            mergesort = ms = ListNode(list2.val, None)
            list2 = list2.next
        

        while True:
            if not list1:
                ms.next = list2
                break
            elif not list2:
                ms.next = list1
                break
            
            if list1.val < list2.val:
                ms.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                ms.next = ListNode(list2.val, None)
                list2 = list2.next
            ms = ms.next

        return mergesort
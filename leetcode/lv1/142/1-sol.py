# 이 링크 참고!
# https://fomaios.tistory.com/entry/Algorithm-Floyds-Cycle-Detection-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%9E%80

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
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None
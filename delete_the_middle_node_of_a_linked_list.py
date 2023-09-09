# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next : return head.next

        slow, fast = head, head
        temp = None

        while fast and fast.next : 
            temp = slow
            fast = fast.next.next
            slow = slow.next
        temp.next = slow.next
        slow.next = None

        return head
        
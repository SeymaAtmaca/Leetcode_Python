# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vall = []
        while True : 
            if head.next:
                vall.append(head.val)
                head = head.next
            else : 
                vall.append(head.val)
                break
        if vall[:] == vall[::-1]:
            return True
        return False
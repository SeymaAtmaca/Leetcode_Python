class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None :
            return list2
        if list2 is None:
            return list1

        new = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val : 
                dummy.next = list1
                list1 = list1.next
            else :
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        if list1 :
            dummy.next = list1
        if list2 :
            dummy.next = list2
        return new.next


# aşağıdaki çözüm daha hızlı 

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         return merge_two_sorted_list(list1, list2)

# def merge_two_sorted_list(list1, list2):
#     if list1 is None:
#         return list2
#     if list2 is None:
#         return list1

#     if list1.val <= list2.val:
#         return ListNode(val=list1.val, next=merge_two_sorted_list(list1.next, list2))
#     else:
#         return ListNode(val=list2.val, next=merge_two_sorted_list(list1, list2.next))
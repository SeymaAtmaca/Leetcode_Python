# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return
        
        ## iterate the list
        node, l = head, [[head.val, head]]
        while node.next:
            node = node.next
            l.append([node.val, node])
            
        l.sort(key=lambda x:x[0])
		
		## reconstruct the list
        node = head = l[0][1]
        for k,v in l[1:]:
            node.next = v
            node = node.next
        node.next = None
        
        return head
        
    # Aşağıdaki kullanım daha hızlı ve daha kullanışlı bir çözüm !!         
        # values = []
        # cur_node = head
        # while cur_node is not None:
        #     values.append(cur_node.val)
        #     cur_node = cur_node.next

        # values = sorted(values)
        # cur_node = head
        # for value in values:
        #     cur_node.val = value
        #     cur_node = cur_node.next
        
        # return head
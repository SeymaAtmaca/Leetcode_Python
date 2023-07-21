# amac, child listeleri duzlestirerek butun listeyi 
# tek liste haline getirmek
# gorsel ornegi readme.md ye birakilmistir

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def flatten_c(node): # alt agaclarin da rahatca islenebilmesi icin olustuurlan yeni fonks.
            tail = node # isleme yapilabilmesi icin yeni node a kopyalandi
            while node: # node lar var oldugu surece , ( burada her liste icin ayri ayri calisma yapilir.)
                if node.child: # eger mevcut node un bir child ı yani alt listesi varsa ;
                    child_tail = flatten_c(node.child) # bu listeyi recursive ile isle
                    child_tail.next = node.next # alt listenin devamini mevcut listenin next ine bagla
                    if node.next: # eger mevcut node, listenin son nodu degilse
                        node.next.prev = child_tail # bir sonraki node un prev ini alt liste olarak ayarla
                    node.child.prev = node # alt listenin prev ini ayarla
                    node.next = node.child # mevcut node un next ini child olarak degistir
                    node.child = None # chil ı kaldir
                    tail = child_tail # tail degiskenini guncelle
                    node = child_tail.next # islemek icin sonraki node a gec
                else: # eger child yoksa
                    tail = node # mevcut node u tail a ata
                    node = node.next # bir sonraki node a gec
            return tail # tail ı dondur

        flatten_c(head)
        return head
    

# LEETCODE da en hizli cozum : 
# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
# """

# class Solution(object):
#     def flatten(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         if not head:
#             return None

#         # create a dummy node to avoid edge case of inserting to empty list
#         dummy = Node(0, None, head, None)
#         stack = [head]
#         prev = dummy

#         while stack:
#             curr = stack.pop()
#             # connect the current node to the previous node
#             prev.next = curr
#             curr.prev = prev

#             if curr.next:
#                 stack.append(curr.next)
#             if curr.child:
#                 stack.append(curr.child)
#                 # set the child node to None
#                 curr.child = None

#             # update the previous node
#             prev = curr

#         newHead = dummy.next
#         newHead.prev = None # set the previous node's next node to None
#         return newHead




# LEETCODE da en az bellek harcayan cozum : 
# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
# """

# class Solution(object):
#     def flatten(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         if not head:
#             return None

#         stack = [head]
#         prev = None

#         while stack:
#             node = stack.pop()
#             if node.next:
#                 stack.append(node.next)

#             if node.child:
#                 stack.append(node.child)
#                 node.child = None

#             if prev:
#                 prev.next = node
#                 node.prev = prev
#             prev = node

#         return head
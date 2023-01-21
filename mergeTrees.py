"""

root1 =         10
            /       \
        2               3


root2 =         10
            /       \
        2               3


sonuç ; 
root1 =         20
            /       \
        4               6

"""


class Node():
    def __init__(self):
        self.val = None
        self.right = None
        self.left = None
        self.next = None

def create(val , root):
    if root.val == None:
        root.val = val
        
    else : 
        p = root
        n = Node()
        n.val = val
        while(1):
            if n.val < p.val :
                if p.left == None:
                    p.left = n
                    print(val, " left için eklendi")
                    break
                else : 
                    p = p.left
                

            else :
                if p.right == None:
                    p.right = n
                    print(val, " right için eklendi")
                    break
                else : 
                    p = p.right




def mergeTrees( root1, root2):

        queue = [(root1, root2)]
        
        
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        while queue:
            node1, node2 = queue.pop(0)
            
            if node2:
                if node2.right:
                    if not node1.right:
                        node1.right = node2.right
                    else:
                        node1.right.val += node2.right.val
                        queue.append((node1.right, node2.right))
                if node2.left:
                    if not node1.left:
                        node1.left = node2.left
                    else:
                        node1.left.val += node2.left.val
                        queue.append((node1.left, node2.left))
        
        return root1 


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

root1 = Node()
create(10, root1)
create(2, root1)
create(3, root1)


root2 = Node()
create(10, root2)
create(2, root2)
create(3, root2)


mergeTrees(root1, root2)
inorder(root1)
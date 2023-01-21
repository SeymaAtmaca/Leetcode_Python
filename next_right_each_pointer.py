#   [1,2,3,4,5,6,7] tree yapısı --> [ 1, #, 2, 3, #, 4,5,6,7, #] şeklinde döndürülür


class Node():
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None
        self.next = None

def create(val):
    if root.data == None:
        root.data=val
    else :
        n = Node()
        n.data=val
        p = root

        while(1):
            if root.data > val:
                if root.left == None:
                    root.left = n
                    break
                else:
                    p = p.left
                
            else:
                if root.right == None:
                    root.right = n
                    break
                else:
                    p = p.right

        
def connect(self,root):
    que = deque()
    que.append(root)

    while que and que[0]:
        length = len(que)
        for i in range(length):
            curr = que.popleft()
            curr.next = que[0] if i+1 < length else None

            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

    return root



root = Node()
class Node():
    def __init__(self):
        self.right = None
        self.left = None
        self.data = None


def create(val):
    if root.data == None:
        root.data = val

    else : 
        p = root
        n = Node()
        n.data = val

        while(1):
            if n.data < p.data :
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


root = Node()
create(10)
create(2)
create(20)
create(35)
create(3)
create(1)


class Node():
    def __init__(self, data):
        self.left = None
        self.right =None
        self.data = data

    def insert(self, data):
        if self.data < data : 
            if self.right == None:
                self.right = Node(data)
            else :
                self.right.insert(data)
        elif self.data > data : 
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
    
    def print_tree(self):
        if self.left != None:
            self.left.print_tree()
        print(self.data)
        if self.right != None:
            self.right.print_tree()


root = Node(5)
root.insert(4)
root.insert(9)
root.print_tree()
        
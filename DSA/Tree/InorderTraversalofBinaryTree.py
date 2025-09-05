class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self,value):
        if self.value == value:
            return #if node already have the same value. 
        
        if value < self.value:
            # left subtree 
            if self.left:
                self.left.add_child(value)
            else:
                # if left root node is empty then strart with new.
                self.left = Node(value)

        else:
            # right subtree
            if self.right:
                self.right.add_child(value)
            else:
                # if right root node is empty then strart with new.
                self.right = Node(value)


def InOrder(elements):
    print(elements)
    root = Node(elements[0])
    print(root.value)

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__ == '__main__':
    elements = [12,7,9,25,17,20]
    root = InOrder(elements)
    print(root)
    pass

class Node:
    def __init__(self, Value):
        self.value = Value 
        self.l_node = None 
        self.r_node = None

    def print(self):
        return self.value

def Insertion(root, value ):
    if root is None:
        return Node(value)
    else:
        print(value)
        if root.value > value:
            if root.l_node is None:
                root.l_node = Node(value)
            else:
                Insertion(root.l_node, value)
        else:
            if root.r_node is None:
                root.r_node = Node(value)
            else:
                Insertion(root.r_node, value)

    
if __name__ == '__main__':
    root = Node(9)
    root.l_node = Insertion(root,5)
    root.r_node = Insertion(root, 12)
    print(root.print())


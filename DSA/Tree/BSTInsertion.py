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
        # print(value)
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

    # Binary Tree
    #         10
    #       /    \
    #     5        20
    #   /   \     /   \
    #  3     7   15    25
    #       / \
    #      6   8

def PreOrder(root):
    # root --> left --> right
    if root:
        print(root.value, end=" ")
        PreOrder(root.l_node)
        PreOrder(root.r_node)
        
def PostOrder(root):
    # left --> right --> root
    if root:
        PostOrder(root.l_node)
        PostOrder(root.r_node)
        print(root.value, end=" ")

def InOrder(root):
    # left --> root --> right
    if root:
        InOrder(root.l_node)
        print(root.value, end=" ")
        InOrder(root.r_node)
    

if __name__ == '__main__':
    root = Node(10)
    root.l_node = Node(5)
    root.r_node = Node(20)
    root.l_node.l_node = Node(3)
    root.l_node.r_node = Node(7)
    root.l_node.r_node.l_node = Node(6)
    root.l_node.r_node.r_node = Node(8)
    root.r_node.l_node = Node(15)
    root.r_node.r_node = Node(25)
    
    print("Preorder traversal:")
    PreOrder(root)
    print("\n")
    print("postorder traversal:")
    PostOrder(root)
    print("\n")
    print("inorder traversal:")
    InOrder(root)

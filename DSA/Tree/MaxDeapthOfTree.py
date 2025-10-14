class Node:
    def __init__(self, val, left=None, right=None) -> None:
            self.val = val 
            self.left = left
            self.right = right 

#         9
#       /   \
#      7     12
#     / \   /  \
#    4   2 15  20
            

def maxDepth(root):
        if root is None:
            return 0 
        
        left = maxDepth(root.left)
        print(left)
        right = maxDepth(root.right)
        # print(right)

        return 1+ max(left, right)


if __name__ == '__main__':
      root = Node(9)
      root.left = Node(7)
      root.left.left = Node(4)
      root.left.left.left = Node(1)
      root.left.right = Node(2)
      root.right = Node(12)
      root.right.left = Node(15)
      root.right.right = Node(20)

      result = maxDepth(root)
      print(result)











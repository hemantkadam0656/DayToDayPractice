class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):

    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
 


# --- Create first tree ---
#        1
#       / \
#      2   3
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# --- Create second tree (same as tree1) ---
#        1
#       / \
#      2   3
tree2 = TreeNode(1)
tree2.left = TreeNode(3)
tree2.right = TreeNode(3)

ans = isSameTree(tree1 , tree2)
print(ans)




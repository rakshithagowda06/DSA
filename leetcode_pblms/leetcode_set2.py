""" Tree problems"""

# maxdepth of a tree 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1+max(left_depth,right_depth)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(10)
print(maxDepth(root))

# Invert a tree


def invertTree(root):
    if not root:
        return None
    
    # Swap using tuple unpacking (more Pythonic!)
    root.left, root.right = root.right, root.left
    
    # Recursively invert
    invertTree(root.left)
    invertTree(root.right)
    
    return root



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
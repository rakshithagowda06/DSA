class TreeNode:
    def __init__(self,val):
        self.val = val # store the value of node
        self.left = None # left child is empty by default
        self.right = None # right child is empty by default


def lowestcommonAncestor(root,p,q):
    node = root  # start traversal from root

    while node: # keep loop untill we find the answer
        if p.val < node.val and q.val < node.val: ## both nodes are smaller than current
            node = node.left                      # move to left subtree
        elif p.val > node.val and q.val > node.val: # both nodes are greater than current
            node = node.right               # move to right subtree
        else:                               # p and q are split OR one of them equals current node
            return node                     # current node is the LCA, return it




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper_func(node,min_val,max_val):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return (helper_func(node.left,min_val,node.val) and
                   helper_func(node.right,node.val,max_val))
        return helper_func(root,float('-inf'),float('inf'))
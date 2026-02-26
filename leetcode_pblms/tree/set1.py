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

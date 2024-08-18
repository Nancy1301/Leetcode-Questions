# 572. Subtree of Another Tree:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Defining helped function to check if it's the same tree of not

        def sameTree(p,q):

            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            if (p.val != q.val):
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def hasSubTree(root):
            if root is None:
                return False
            
            if sameTree(root, subRoot):
                return True
            
            return hasSubTree(root.left) or hasSubTree(root.right)
        
        return hasSubTree(root)

        
        

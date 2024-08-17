# 543. Diameter of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_depth = [0]
        def height(root):

            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            depth =  left + right 
            max_depth[0] = max(max_depth[0], depth)

            return 1 + max(left, right)

        height(root)
        return max_depth[0]

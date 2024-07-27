# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def is_sym(left, right):
            if left is None and right is None:
                return True
            
            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            return is_sym(left.left, right.right) and is_sym(left.right, right.left)
        
        return is_sym(root.left, root.right)
        
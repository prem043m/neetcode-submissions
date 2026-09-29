# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def cal_height(root):
            if not root:
                return 0

            left_height = cal_height(root.left)
            right_height = cal_height(root.right)
            
            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1 :
                return -1
            return 1 + max(left_height,right_height)
        if cal_height(root) == -1:
            return False
        return True
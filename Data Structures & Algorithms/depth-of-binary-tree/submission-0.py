# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDepth(self,root):
        if not root :
            return 0
        leftDepth = 1 + self.findDepth(root.left)
        rightDepth = 1 + self.findDepth(root.right)

        return max(leftDepth,rightDepth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findDepth(root)
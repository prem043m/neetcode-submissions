# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            q_size = len(q)
            curr_level = []

            for _ in range(q_size):
                node = q.popleft()
                curr_level.append(node.val)

                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            result.append(curr_level[-1])
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 0
    current_depth = 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            self.max_depth = self.current_depth-1 if self.current_depth > self.max_depth else self.max_depth
            return self.max_depth
        self.current_depth += 1
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.current_depth -= 1
        return self.max_depth
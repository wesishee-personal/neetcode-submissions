# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}

        def levelOrderTraverse(node, currentDepth):
            if not node:
                return

            if currentDepth not in result:
                result[currentDepth] = []

            result[currentDepth].append(node.val)
            levelOrderTraverse(node.left, currentDepth+1)
            levelOrderTraverse(node.right, currentDepth+1)

        levelOrderTraverse(root, 0)
        return list(result.values())
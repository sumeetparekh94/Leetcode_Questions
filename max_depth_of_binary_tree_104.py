# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthHelper(root)

    def maxDepthHelper(self, node):
        max_depth = 1
        if node == None:
            return 0

        else:
            left_height = self.maxDepthHelper(node.left)
            right_height = self.maxDepthHelper(node.right)
            return max(left_height, right_height) + 1
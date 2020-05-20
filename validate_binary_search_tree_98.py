# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math


class Solution:
    def bst_helper(self, node, min_value, max_value):

        if node == None:
            return True

        if not min_value < node.val < max_value:
            return False

        return (self.bst_helper(node.left, min_value, node.val) and
                self.bst_helper(node.right, node.val, max_value))

    def isValidBST(self, root: TreeNode) -> bool:

        return self.bst_helper(root, -math.inf, math.inf)


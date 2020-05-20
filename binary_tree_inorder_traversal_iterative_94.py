# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        curr = root
        res = []

        while True:

            if curr:

                stack.append(curr)
                curr = curr.left

            elif stack:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right

            else:
                break

        return res

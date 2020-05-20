# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        if root == None:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            current_level = []
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            res.append(current_level)

        return res

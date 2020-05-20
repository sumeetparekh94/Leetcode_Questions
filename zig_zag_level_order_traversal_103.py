# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque()
        queue.append(root)
        flag = False
        while queue:
            current_level = deque()
            level_size = len(queue)

            for _ in range(level_size):
                curr_node = queue.popleft()
                if not flag:
                    current_level.append(curr_node.val)
                else:
                    current_level.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            res.append(current_level)
            flag = not flag

        return res

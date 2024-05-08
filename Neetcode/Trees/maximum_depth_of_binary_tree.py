# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_max_depth(self, root, depth):
        if not root:
            return depth

        return max(self.get_max_depth(root.left, depth + 1), self.get_max_depth(root.right, depth + 1))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.get_max_depth(root, 0)


        
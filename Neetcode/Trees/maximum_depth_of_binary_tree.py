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


"""
iterative solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
   

"""
        
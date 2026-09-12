# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSum(self, root, result):
        if not root:
            return 0
        
        left_sum = self.maxSum(root.left, result)
        right_sum = self.maxSum(root.right, result)

        path_sum = root.val + left_sum + right_sum

        result[0] = max(result[0], path_sum)

        return max(0, root.val + left_sum, root.val + right_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]
        self.maxSum(root, result)

        return result[0]
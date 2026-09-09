# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findKthSmallest(self, root, count):

        if not root:
            return -1

        leftNode = self.findKthSmallest(root.left, count)
        count[0] -=1
        if count[0] == 0:
            return root.val
        rightNode = self.findKthSmallest(root.right, count)

        if leftNode > -1:
            return leftNode
        if rightNode > -1:
            return rightNode
        
        return -1



    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        count = [k]

        return self.findKthSmallest(root, count)
        

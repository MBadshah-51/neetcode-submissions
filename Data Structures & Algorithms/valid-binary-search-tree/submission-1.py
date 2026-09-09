# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkTree(self, root, lowerBound, upperBound):
        if not root:
            return True
        if lowerBound < root.val < upperBound:
            return self.checkTree(root.left, lowerBound, root.val) \
                and self.checkTree(root.right, root.val, upperBound)
            
        return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.checkTree(root, float('-inf'), float('inf'))
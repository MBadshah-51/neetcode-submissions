# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd, dt):
        if preStart > preEnd or inStart > inEnd:
            return None
        
        root = TreeNode(preorder[preStart])
        inRoot = dt[root.val]
        numsleft = inRoot - inStart
        root.left = self.build(preorder, preStart + 1, preStart + numsleft, inorder, inStart, inRoot - 1, dt)
        root.right = self.build(preorder, preStart + numsleft + 1, preEnd, inorder, inRoot + 1, inEnd, dt)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) != len(inorder):
            return None

        dt = {val: idx for idx, val in enumerate(inorder)}

        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder) - 1, dt)
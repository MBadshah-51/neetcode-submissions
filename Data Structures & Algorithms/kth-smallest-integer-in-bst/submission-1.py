# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, count):

        from collections import deque
        st = deque()
        curr = root

        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            count -= 1
            if count == 0:
                return curr.val
            curr = curr.right
        
        return -1
            

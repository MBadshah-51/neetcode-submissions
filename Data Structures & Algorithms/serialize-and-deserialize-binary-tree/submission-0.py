# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        from collections import deque

        que = deque()

        que.append(root)

        ans = []

        while que:
            node = que.popleft()

            if not node:
                ans.append("#")
            else:
                ans.append(str(node.val))
                que.append(node.left)
                que.append(node.right)

        print(ans)
        
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "#": 
            return None

        root = TreeNode(int(vals[0]))
        from collections import deque
        que = deque()
        que.append(root)
        idx = 1

        while que:
            node = que.popleft()

            if vals[idx] != "#":
                left_child = TreeNode(int(vals[idx]))
                node.left = left_child
                que.append(left_child)
            idx += 1

            if vals[idx] != "#":
                right_child = TreeNode(int(vals[idx]))
                node.right = right_child
                que.append(right_child)
            idx += 1
        
        return root


        



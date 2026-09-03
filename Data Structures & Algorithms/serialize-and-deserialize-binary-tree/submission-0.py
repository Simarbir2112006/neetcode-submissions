# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.arr = []

        def dfs(node):
            if not node:
                self.arr.append('N')
                return
            
            self.arr.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(root)
        return ",".join(self.arr)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        self.i = 0
        def dfs():
            val = arr[self.i]
            self.i += 1
            if val == 'N':
                return None
            
            node = TreeNode(val = int(val))
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()


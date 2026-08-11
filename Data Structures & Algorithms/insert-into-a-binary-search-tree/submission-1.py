# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.new_node = TreeNode(val)

        if not root:
            return self.new_node

        def dfs(node, val):
            if node.right and node.val < val:
                return dfs(node.right, val)

            elif node.left and node.val > val:
                return dfs(node.left, val)
            
            elif node.val > val:
                node.left = self.new_node
                return
            
            else:
                node.right = self.new_node
                return
        
        dfs(root, val)

        return root
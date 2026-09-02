# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        idxs = {inorder[i]: i for i in range(n)}

        def maker(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e:
                return

            root = TreeNode(preorder[pre_s])
            mid = idxs[preorder[pre_s]]

            root.left = maker(pre_s + 1, pre_s + (mid - in_s), in_s, mid)
            root.right = maker(pre_s + (mid - in_s) + 1, pre_e, mid+1, in_e)

            return root
        
        return maker(0, n - 1, 0, n - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root):
            #return none if its empty
            if not root:
                return None
            
            #if the root is the required number it is the LCA
            #return immediately without searching the rest
            if root.val == p or root.val == q:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            #if both p and q is present in the subtree then root is the LCA
            if left and right:
                return root
            #if only one value present in the subtree , that one is the LCA
            return left if left else right
        # return dfs(root)

        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
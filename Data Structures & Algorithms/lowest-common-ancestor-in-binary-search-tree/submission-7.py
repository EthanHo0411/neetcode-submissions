# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root, node):
            #base case not found 
            if not root:
                return False
            
            #found 
            if root.val == node.val: 
                return True
            
            #continue searching
            return dfs(root.left, node) or dfs(root.right, node)

        #base case 
        if not root:
            return None
            
        left = root.left 
        right = root.right 
        pl = dfs(left, p) 
        pr = dfs(right, p)
        ql = dfs(left, q)
        qr = dfs(right, q)
        #check if the root is p or q 
        if root.val == p.val: 
            return p if ql or qr else None
        elif root.val == q.val: 
            return q if pr or pl else None
        elif (pl and qr) or (pr and ql):
            return root
        else: 
            return (self.lowestCommonAncestor(left, p , q) or self.lowestCommonAncestor(right, p , q))

        
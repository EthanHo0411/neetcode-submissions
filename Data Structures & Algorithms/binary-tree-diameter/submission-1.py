# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left  1
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #use the res variable for global storage of best diameter
        #since its number of edges, dont count the root
        res = 0 
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left)
            right =dfs(root.right)
            res = max(res, left + right)
            return 1+max(left,right)
        
        dfs(root)
        return res

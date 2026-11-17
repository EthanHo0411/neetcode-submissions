# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #the nature of BST means that there will be boundary for each node depending on its position
        #the idea is to inherit the boundary as it goes down the tree and check if the value is within the bound

        def dfs(root, lower ,upper):
            if not root:
                return True
            
            current = (lower <root.val < upper)
            return current and dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
        
        return dfs(root, float("-inf"),float("inf"))

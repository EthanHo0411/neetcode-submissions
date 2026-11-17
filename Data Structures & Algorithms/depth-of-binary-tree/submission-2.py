# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #keep going to the farthest right or left
        def dfs(root):
            #base case when root is null 
            if not root:
                return 0
            
            #keep going to the left or right 
            left = 1+ dfs(root.left)
            right = 1 + dfs(root.right)
            return max(left, right)
        return dfs(root)

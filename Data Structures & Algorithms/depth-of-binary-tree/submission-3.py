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
            #when it reaches the end returns 0
            if not root: 
                return 0
            
            #keep navigate to the left and right of the tree
            #gets the max length before returning up to the root
            return max(dfs(root.left), dfs(root.right)) + 1
        return dfs(root)
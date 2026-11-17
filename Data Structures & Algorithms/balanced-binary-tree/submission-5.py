# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            #base case empty root means balanced 
            if not root:
                return [0 , True]

            #check if the left and right have the same height
            #check if they are balanced individually

            leftH, leftB = dfs(root.left)
            rightH, rightB = dfs(root.right)

            return [max(leftH, rightH) + 1, (0 <= abs(leftH - rightH) <= 1) and leftB and rightB]
        
        return dfs(root)[1]

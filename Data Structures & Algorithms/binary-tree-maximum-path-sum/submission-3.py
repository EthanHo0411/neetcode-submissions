# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #handles the case of all negative nodes
        res = float("-inf")
        def dfs(root):
            nonlocal res
            #base case of 0 value
            if not root:
                return 0
            
            #get the max number from the left branch and the right branch
            #this make sure the contribution of the branch is at least 0
            left = dfs(root.left)
            left = max(0,left)
            right = dfs(root.right)
            right = max(0,right)
            #compare the current path against the current max
            res = max(res, left+right+root.val)
            #at the end return the max length branch plus the root value
            #since the left and right branch is at least 0
            #it implies that it dont have to carry the negative branch value up to the higher levels 
            return root.val+max(left,right)
        
        temp = dfs(root)
        return res

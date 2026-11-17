# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            #make sure the contribution of the lef and right branch is at least 0
            left = max(dfs(root.left), 0 )
            right = max(dfs(root.right), 0)
            #check if the whole path atm is larger than the current max
            res = max(res, left+right+root.val)
            return max(left,right)+root.val
        
        dfs(root)
        return res
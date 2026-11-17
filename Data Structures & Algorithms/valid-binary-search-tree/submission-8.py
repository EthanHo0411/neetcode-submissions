# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #beside checking for left < root< right
        #the intuition is that the each node would have a range they can go
        #its value has to be within the range
        def dfs(root, lower, upper):
            if not root:
                return True
            
            #check if the current node is within the range of value
            limit = lower < root.val < upper

            #update the range for the descdents
            #if its the left branch of a node on a right branch, it would have a min limit
            #if its the right branch of a node on a left branch, it has a max limit

            #check the conditions and update threshold for the rest of the branches
            return limit and dfs(root.left,lower,root.val) and dfs(root.right, root.val , upper)
        return dfs(root, float("-inf"),float("inf"))

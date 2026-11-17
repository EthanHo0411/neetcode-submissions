# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#use a helper recursive function to pass down the tree
#at each layer, recursively call the left and right subtree
#check if the boolean for left and right is true and also if they have the same length
#finally return the condition result and also the max length so far


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True,0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and (abs(left[1]-right[1]) <= 1)

            return [balanced, 1+max(left[1], right[1])]
        
        return dfs(root)[0]
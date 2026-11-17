# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxlen = 0

        #basically means from the farthest left node to the farthest right node of the tree 
        def dfs(root):

            nonlocal maxlen 

            if not root: 
                return 0

            #check the diameter of the left and right
            left = dfs(root.left)
            right =  dfs(root.right)

            #update the max diameter by joining the branches with root 
            length = left + right 
            maxlen = max(length , maxlen)

            #return the max length including the root to the upper call 
            return max(left, right) +1 
        
        number = dfs(root)

        return maxlen
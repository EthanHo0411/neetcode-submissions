# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #since the nature of BST is having number less than the root on the left
        #and number larger than the root on the right
        #it naturally form a ascending sequence of numbers
        #the idea is append the item starting from the leftmost node
        #then the root , and then the right item. repeat until rightmost

        res = []
        def dfs(root):

            #base case
            if not root:
                return 
            
            #append the left ,then root, then the right
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

            return
        dfs(root)
        return res[k-1]
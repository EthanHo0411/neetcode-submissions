# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case of a null tree also a subtree of the main tree
        if not subRoot:
            return True
        #if the subroot is present and root is null then its not subtree
        if not root:
            return False

        #if they are the same tree they are subtree
        if self.sameTree(root, subRoot):
            return True
        
        #recursive call to check for subtree
        return (self.isSubtree(root.left, subRoot) or 
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case where both root are null
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                   self.sameTree(root.right, subRoot.right))
        return False
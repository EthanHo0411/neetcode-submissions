# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subroot):
            #base case both completes or is empty 
            if not root and not subroot: 
                return True 
            
            #recursively calls its lower branches 
            if root and subroot and root.val == subroot.val: 
                return isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right)
            
            return False

        if not subRoot:
            return True 
        if not root:
            return False

        #iterate through each node and check if a tree is present
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

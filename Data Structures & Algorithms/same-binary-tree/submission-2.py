# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            #base case, if both root is empty , return true
            if not p and not q:
                return True
            #if one of them is empty , its not the same tree
            elif not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            #now the current node is checked to be the same
            #recursively going to the left and right tree of each node
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            #if both are true, it means the they are the same for the subtree as well
            #in that case its the same tree as to this point
            return left and right
        
        def dfs_optimal (p,q):
            if not p and not q:
                return True
            if p and q  and p.val == q.val:
                return (dfs_optimal(p.left, q.left) and dfs_optimal(p.right, q.right)) 
            return False 
        return dfs_optimal(p,q)


        
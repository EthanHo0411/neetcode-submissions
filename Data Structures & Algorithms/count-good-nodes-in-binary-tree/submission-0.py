# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        def dfs (root, max_value):
            if not root:
                return None
            
            maxx = max_value
            if max_value <= root.val:
                result.append(root.val)
                maxx = root.val
            
            #go to the left and right branch
            left = dfs(root.left,maxx) 
            right = dfs(root.right,maxx)
            return None
        temp = dfs(root,float("-inf"))
        return len(result)
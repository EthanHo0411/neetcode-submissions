# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        # Create the root node from the first element of preorder
        root = TreeNode(preorder[0])
        
        # Find the position of the root in inorder
        index = inorder.index(preorder[0])
        
        # Split inorder array
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]
        
        # Split preorder array based on the size of left subtree
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        
        # Recursively build left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root
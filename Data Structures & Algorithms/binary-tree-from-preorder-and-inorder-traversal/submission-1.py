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
            #base case of creating a single node with no descdents
            if len(inorder) == 1:
                return TreeNode(inorder[0], None, None)
            
            #first identiy the root in each segment 
            #the first element of the preorder array
            #create the root node
            root = TreeNode(preorder[0])

            #search for this root node in the inorder array
            #to create the split of left and right branch
            index = inorder.index(preorder[0])
            left = inorder[:index]
            right = inorder[index+1:]
            
            #preform the left and right recursion and allow the function to return the left and right node
            #connect to the current root
            left = self.buildTree(preorder[1:index+1],left)
            right = self.buildTree(preorder[index+1:],right)
            root.left = left
            root.right = right
            return root



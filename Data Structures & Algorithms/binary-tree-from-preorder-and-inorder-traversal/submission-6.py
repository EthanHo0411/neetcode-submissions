# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #the idea is that first item of the preorder is the root 
        #so we can use this root to find the point of separation in the preorder array 
        #separating the preorder array into left, root and right
        #now the left part would be the left subtree of the current root
        #we can do recursion with that left segment and grab the same length after the root in the preorder array
        #this way we know how many items are in the left and right subtree
        
        #base case 
        if not preorder or not inorder:
            return None
        
        #extract the root from the preorder array
        item = preorder[0]
        root = TreeNode(item)

        #find the split in the inorder array
        index = inorder.index(item)
        #construct the new inorder and preorder segments
        left_in = inorder[:index]
        right_in = inorder[index+1:]
        left_pre = preorder[1:1+index]
        right_pre = preorder[1+index:]

        #iterate to create the left and right subtree
        left = self.buildTree(left_pre,left_in)
        right = self.buildTree(right_pre,right_in)

        #link it to the root
        root.left = left
        root.right = right

        #return the root
        return root
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hash map for inorder elements
        # This maps each value to its index in the inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(prestart, preend, instart, inend):
            if prestart > preend:
                return None
                
            # Root value is the first element in current preorder segment
            root_val = preorder[prestart]
            root = TreeNode(root_val)
            
            # Find position of root in inorder using hash map (O(1) operation)
            inorder_idx = inorder_map[root_val]
            
            # Calculate size of left subtree
            left_size = inorder_idx - instart
            
            # Recursively build left and right subtrees
            root.left = build(prestart + 1, prestart + left_size, instart, inorder_idx - 1)
            root.right = build(prestart + left_size + 1, preend, inorder_idx + 1, inend)
            
            return root
            
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        from collections import deque
        if not root:
            return ""
        nodes = deque([root])
        temp = []
        res = [str(root.val)]
        while nodes:
            node = nodes.popleft()

            if node.left:
                res.append(str(node.left.val))
                temp.append(node.left)
            else:
                res.append("None")
            
            if node.right:
                res.append(str(node.right.val))
                temp.append(node.right)
            else:
                res.append("None")
            
            if not nodes:
                if temp:
                    nodes.extend(temp)
                    temp = []
        return " ".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        #split the string into list and then convert to integers or None
        nodes = data.split()
        nodes = [int(node) if node != "None" else None for node in nodes]
        
        #create the top root
        root = TreeNode(nodes[0])
        #perform level order traversal to construct the tree
        from collections import deque 
        nodes = deque(nodes[1:])
        #for holding the current level of nodes
        current = deque([root])
        temp = []
        while nodes:
            #get the current node to be linked
            node = current.popleft()

            #get the left and right of the current node
            left = nodes.popleft()
            left = TreeNode(left) if left else None
            right = nodes.popleft()
            right = TreeNode(right) if right else None
            node.left = left
            node.right = right
            #add the nodes to the linking list if not None
            if left:
                temp.append(left)
            if right:
                temp.append(right)
            
            if not current:
                if temp:
                    current.extend(temp)
                    temp = []
        return root


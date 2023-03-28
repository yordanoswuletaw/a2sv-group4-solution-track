# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        new_node = TreeNode(val)
        if not root:
            return new_node
        
        prev, curr = None, root
        while curr:
            prev = curr 
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left 
        
        if prev.val > val:
            prev.left = new_node
        else:
            prev.right = new_node 
        
        return root

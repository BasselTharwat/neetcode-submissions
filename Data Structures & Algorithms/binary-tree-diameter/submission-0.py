# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # I want to return the sum of the height of the left subtree and the right subtree
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        # returns the maximum height between the left subtree and the right subtree
        def height(curr: TreeNode):
            if curr is None:
                return 0 

            leftHeight = height(curr.left)
            rightHeight = height(curr.right)

            # Here, we update the result variable to have the new sum of heights
            self.result = max(self.result, leftHeight + rightHeight)
            
            return 1 + max(leftHeight , rightHeight)

        height(root)

        return self.result
            


        
        
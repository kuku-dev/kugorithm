# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root, sumVal):
            if root == None:
                return False
            sumVal += root.val
            if root.left == None and root.right == None:
                if sumVal == targetSum:
                    return True
            return pathSum(root.left, sumVal) or pathSum(root.right, sumVal)
        return pathSum(root, 0)
        
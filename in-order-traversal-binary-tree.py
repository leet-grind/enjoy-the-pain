# This is from Leetcode - LC 94: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(r, res):
            if not r:
                return res
            helper(r.left, res)
            res.append(r.val)
            helper(r.right, res)
            return res
        return helper(root, [])

# Post Order Traversal in binary tree - LC 145
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(r, res):
            if not r:
                return res
            helper(r.left, res)
            helper(r.right, res)
            res.append(r.val)
            return res
        return helper(root, [])

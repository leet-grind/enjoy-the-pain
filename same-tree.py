# Leetcode 100 - Same Tree Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p and q:
            if q.val != p.val:
                return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

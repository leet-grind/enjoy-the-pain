# Leetcode 653 Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        def in_ord(r, res):
            if not r:
                return res
            in_ord(r.left, res)
            res.append(r.val)
            in_ord(r.right, res)
            return res
        vals = in_ord(root, [])
        left = 0
        right = len(vals)-1
        while left < right:
            curr_sum = vals[left]+vals[right]
            if curr_sum == k:
                return True
            elif curr_sum > k:
                right -= 1
            else:
                left += 1
        return False

# Climbing Stairs - Leetcode 70 Dynamic Programming
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        res = [1, 2]
        for ind in range(2, n):
            res.append(res[-1]+res[-2])
        return res[-1]

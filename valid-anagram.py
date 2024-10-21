class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        freqs = {}
        for char in s:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
        for each in t:
            if each not in freqs:
                return False
            else:
                freqs[each] -= 1
        for each in freqs:
            if freqs[each] != 0:
                return False
        return True

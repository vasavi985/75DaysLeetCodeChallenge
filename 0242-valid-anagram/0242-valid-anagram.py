class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w=sorted(s)
        g=sorted(t)
        if w==g:
            return True
        else:
            return False        
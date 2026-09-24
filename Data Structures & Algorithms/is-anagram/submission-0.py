class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1=collections.Counter(s)
        d2=collections.Counter(t)
        if d1==d2:
            return True
        else:
            return False
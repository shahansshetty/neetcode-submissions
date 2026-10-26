class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a_dict=collections.Counter(s)
        b_dict=collections.Counter(t)
        
        if a_dict==b_dict:
            return True
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s2) < len(s1):
            return False

        n1,n2=len(s1),len(s2)
        counted_s1=Counter(s1)
        
        for i in range(0,n2-n1+1):
            if counted_s1 == Counter(s2[i:i+n1]):
                return True
        return False

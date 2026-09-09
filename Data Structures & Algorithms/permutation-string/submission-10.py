
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        if len(s1)>len(s2):
            return False
            
        d1=collections.Counter(s1)
        
        n1=len(s1)
        n2=len(s2)
        
        for i in range(0,len(s2)-len(s1)+1):
            
            if d1==collections.Counter(s2[i:i+n1]):
                return True
            

        


        return False

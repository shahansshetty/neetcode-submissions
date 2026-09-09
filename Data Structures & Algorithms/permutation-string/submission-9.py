
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        if len(s1)>len(s2):
            return False
            
        d1=collections.Counter(s1)
        l=0
        r=len(s1)-1
        while l<=(len(s2)-len(s1)):
            
            if d1==collections.Counter(s2[l:(r+1)]):
                return True
            l+=1
            r+=1

        


        return False

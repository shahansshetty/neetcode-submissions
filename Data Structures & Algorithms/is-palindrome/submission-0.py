class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.replace(' ','')
        s=s.lower()
        print(s)
        is_pali=False
        string=str()
        for alpha in s:
            if alpha.isalnum():
                string+=alpha

        if string==string[::-1]:
            is_pali=True


        return is_pali
            
        
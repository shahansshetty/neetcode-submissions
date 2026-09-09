class Solution:

    def encode(self, strs: List[str]) -> str:
        string=str()
        for s in strs:
            string+='|'+''.join(s)
            
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        s=s[1:]
        l=[]
        l=s.split("|")
        # for i in s:
        #     if i==',':

        return l


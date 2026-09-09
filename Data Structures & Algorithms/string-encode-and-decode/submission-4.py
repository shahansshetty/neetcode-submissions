class Solution:
    def __init__(self):
        self.map={}
        self.counter=0

    def encode(self, strs: List[str]) -> str:
        key=self.counter
        for s in strs:
            if s not in self.map:
                self.map[key]=strs
            self.counter+=1
            
        # for s in strs:
        #     string=string+ord(s)

        return 'enc'+ str(key)


    def decode(self, s: str) -> List[str]:
        key=int(s.lstrip('enc'))

        return self.map.get(key,[])


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs==[""]:
            return [[""]]
        
        d={}

        for string in strs:
            s_string="".join(sorted(string))
            if s_string not in d:
                d[s_string]=[]
            d[s_string].append(string)

        return list(d.values())


        
        
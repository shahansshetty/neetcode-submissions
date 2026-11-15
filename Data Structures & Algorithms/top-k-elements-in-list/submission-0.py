class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=collections.Counter(nums)
        res=[]
        
        for i in range(k):
            max_ele=max(count,key=count.get)
            count.pop(max_ele)
            res.append(max_ele)
        
        return res
            
        
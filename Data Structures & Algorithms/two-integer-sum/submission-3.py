class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,val in enumerate(nums):
            element = target-val
            if element in d:
                return [d[element],i]
            d[val]=i
        
        
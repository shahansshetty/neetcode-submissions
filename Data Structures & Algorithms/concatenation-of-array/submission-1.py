class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*(2*len(nums))
        l=len(nums)
        for i,num in enumerate(nums):
            ans[i]=ans[i+l]=num
        return ans
        
        
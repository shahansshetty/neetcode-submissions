class Solution:
    def findMin(self, nums: List[int]) -> int:
        # i=0
        # while nums[i] is not None:
        #     if nums[i]>nums[i+1]:
        #         return nums[i+1]
        #     i+=1
        # return nums[0]
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]
            i+=1
        return nums[0]

        
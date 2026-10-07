class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==1:
                mid+=1
                continue
            elif nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            else :
                nums[mid],nums[high]=nums[high],nums[mid]
                
                high-=1


        """
        Do not return anything, modify nums in-place instead.
        """
        
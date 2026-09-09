class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        count=0

        for i in range(length):
            leftmax=rightmax=height[i]

            for j in range(i):
                leftmax=max(leftmax,height[j])
            
            for j in range(i+1,length):
                rightmax=max(rightmax,height[j])

            print(f"leftmax:{leftmax}, rightmax:{rightmax}")
            count+=min(leftmax,rightmax)-height[i]
            
    
        return count
            
        
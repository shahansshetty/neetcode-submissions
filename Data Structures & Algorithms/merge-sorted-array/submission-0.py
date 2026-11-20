class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr_1=m
        ptr_2=0
        print(ptr_1,ptr_2)
        while ptr_1<m+n:
            nums1[ptr_1]=nums2[ptr_2]
            ptr_1+=1
            ptr_2+=1
        nums1.sort()


        """
        Do not return anything, modify nums1 in-place instead.
        """
        
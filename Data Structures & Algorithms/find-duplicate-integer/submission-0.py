class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=collections.Counter(nums)
        for  key , value in d.items():
            if value>1:
                return key
                
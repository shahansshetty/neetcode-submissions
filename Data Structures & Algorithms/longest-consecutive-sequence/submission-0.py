class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest=0
        nums_set=set(nums)
        start_seq=set()
        for i in nums_set:
            if i-1 not in nums_set:
                start_seq.add(i)
        print(start_seq)
        for num in start_seq:
            temp=1
            print(num)
            while num + 1 in nums_set:
                print('while flag , num:',num)
                num+=1
                temp+=1
            print('temp : ',temp,'longest:',longest)
            longest=max(longest,temp)
            

        return longest
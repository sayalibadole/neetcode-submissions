class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count=0
        longest=0
        num_set= set(nums)

        for i, num in enumerate(num_set):
            if num-1 not in num_set: #start of the sequence
                count=1
                while(num+ 1 in num_set):
                    count+=1
                    num+=1
                longest=max(count,longest)
        return(longest)
        
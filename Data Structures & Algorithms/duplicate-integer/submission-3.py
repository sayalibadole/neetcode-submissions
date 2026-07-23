class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup={}
        for i, num in enumerate(nums):
            if num not in dup:
                dup[num]= 1
            else:
                return(True)
        return(False)
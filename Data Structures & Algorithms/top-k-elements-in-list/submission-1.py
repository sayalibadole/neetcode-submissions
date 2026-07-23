class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # count freq and store in hashmap 
        freq={}

        for num in nums:
            freq[num]= freq.get(num,0)+1

    # crete buckets 
        buckets= [[] for i in range(len(nums)+1)]

    # append feq as index and num as values 
        for num, count in freq.items():
            buckets[count].append(num)

    # traverse backwards - add k numbers
        results= []
        for frequency in range(len(buckets)-1, 0, -1):
            for num in buckets[frequency]:
                results.append(num)

                if len(results)==k:
                    return(results)

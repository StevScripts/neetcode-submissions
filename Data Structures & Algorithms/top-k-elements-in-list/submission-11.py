class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHash = {}

        for num in nums:
            countHash[num] = 1 + countHash.get(num,0)

        countHash = dict(sorted(countHash.items(),key=lambda item:item[1],reverse = True))
        sortedList = list(countHash.keys())
        
        return sortedList[:k]
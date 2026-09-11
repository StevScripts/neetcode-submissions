class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Use a counter to see how many of each number there is
        #Sort the counted list
        #ad-d to the list for K times

        sortedNums = Counter(nums).most_common()
        toRet = []
        for i in range(k):
            toRet.append(sortedNums[i][0])

        return toRet
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap with counter, sort ascending
        numsC = Counter(nums)
        print(numsC)

        toRet = []
        mostCom = (numsC.most_common())

        for i in range(k):
            toRet.append(mostCom[i][0])

        return toRet
        


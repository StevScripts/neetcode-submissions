class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxh = [-n for n in stones]

        heapq.heapify(maxh)

        while len(maxh) > 1:
            one,two = heapq.heappop(maxh), heapq.heappop(maxh)

            print(maxh)
            if one < two:
                heapq.heappush(maxh, one - two)
            
        return -maxh[0] if maxh else 0

            

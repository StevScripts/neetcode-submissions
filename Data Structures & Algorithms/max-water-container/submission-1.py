class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Brute force - Loop through each val, find largest O(n^2)

        -Keep track of the max
        -Calculate water by (r-l) * min(heights[l],heights[r])
        -Move l if r >=l
        -Move r if r<l

        '''

        curMax = 0
        l,r = 0,len(heights)-1

        while l<r:
            waterHeld = (r-l) * min(heights[l],heights[r])
            curMax = max(waterHeld,curMax)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return curMax
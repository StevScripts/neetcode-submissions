class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1

        '''
        target = 3
              rl    
        [-1,0,2,4,6,8]
        '''

        '''
        1. calculate middle
        2.if middle < target -> l = m + 1
        3.if middle > target -> r = m - 1


        '''

        while l <= r:
            m = l + ((r-l)//2)

            if nums[m] < target:
                l = m +1
            elif nums[m] > target:
                r = m -1
            else:
                return m
        
        return -1
       
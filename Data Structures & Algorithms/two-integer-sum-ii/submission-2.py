class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''
        normal two sum, space comp O(n)
        O(1), just variables holding the index's
        l      r
        [1,2,3,4]

        l+r > target: r -= 1
        l+r < target: l += 1
        l+r == target: return [l+1,r+1]


        '''

        l,r = 0, len(numbers)-1
        
        while l < r:
            tot = numbers[l] + numbers[r]
            if tot > target:
                r -=1
            elif tot < target:
                l += 1
            else:
                return [l+1,r+1]
            

        
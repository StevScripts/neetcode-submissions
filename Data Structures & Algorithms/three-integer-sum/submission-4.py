class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        -Optimal
        -Tracking a current anchor point
        -using l and r pointer
        -moving l if the sum of l+r+anchor < 0
        -moving r if the sum of l+r+anchor > 0
        -if sum of all three zero, track thise points

        -returning list of lists
                   
        [-4,-1,-1,0,1,2]

        [-1,-1,2],[-1,0,1]
        '''

        ret = []
        nums.sort()

        for i,anchor in enumerate(nums):
            if i > 0 and anchor == nums[i-1]:
                continue

            l,r = i+1,len(nums)-1

            while l < r:
                threeSum = nums[l]+nums[r]+anchor
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r-=1
                else:
                    ret.append([anchor,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return ret



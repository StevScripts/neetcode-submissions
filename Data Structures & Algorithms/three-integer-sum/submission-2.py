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
        l,r = None,None
        anchor = None

        nums.sort()

        for i in range(len(nums)-2):
            anchor = nums[i]
            l,r = i+1,len(nums)-1

            while l < r:
                if nums[l]+nums[r]+anchor < 0:
                    l += 1
                elif nums[l]+nums[r]+anchor > 0:
                    r-=1
                else:
                    toAdd = [anchor,nums[l],nums[r]]
                    if toAdd not in ret:
                        ret.append(toAdd)
                    r-=1
                    l+=1

        return ret



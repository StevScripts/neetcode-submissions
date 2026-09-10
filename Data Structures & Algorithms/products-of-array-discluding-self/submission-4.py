class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        
        '''
        product = 1
        hasZero = False
        ret = []

        for i in range(len(nums)):
            if nums[i] == 0:
                hasZero = True
                continue
            product = product * nums[i]

        print()
        for i in range(len(nums)):
            if hasZero:
                if nums[i] == 0 and Counter(nums)[0] <= 1:
                    ret.append(product)
                else:
                    ret.append(0)
                continue

            ret.append(product//nums[i])

        return ret


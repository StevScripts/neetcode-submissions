class NumArray:

    def __init__(self, nums: List[int]):

        #Start with original start
        #fill in array with pSum[i] = pSum[i-1] + nums[i]
        self.prefix = [0] * (len(nums)+1)

        self.prefix[0] = nums[0]
        for i in range(len(nums)):
            self.prefix[i] = self.prefix[i-1] + nums[i]

        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []

        curSubset = []

        def dfs(i):
            if i >= len(nums):
                allSubsets.append(curSubset.copy())
                return
            
            curSubset.append(nums[i])
            dfs(i+1)

            curSubset.pop()
            dfs(i+1)

        dfs(0)

        return allSubsets
        
        
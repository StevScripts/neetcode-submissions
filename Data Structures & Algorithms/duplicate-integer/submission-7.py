class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenItems = set()
        for num in nums:
            if num in seenItems:
                return True
            seenItems.add(num)

        return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        brute force, make another array, store seen vals
        then check if the character that you are going to add
        is in the array, keep track of max
        '''

        res = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r-l + 1)
        
        return res
            


        
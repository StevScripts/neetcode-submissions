class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #Keeping track of our char occurences
        res = 0 #Longest substring we can create with K replacements

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])

            while (r-l +1) - maxf > k:
                count[s[l]] -= 1
                l+= 1

            res = max(res, r-l +1)

        return res
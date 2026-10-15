class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        Make two hashmaps, count the chars for each
        return if hash1 == hash2

        Questions?
        do hashmaps need chars to be recorded in a specific order
        '''

        hash1,hash2 = {},{}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in hash1:
                hash1[s[i]] += 1
            else:
                hash1[s[i]] = 1

                
            if t[i] in hash2:
                hash2[t[i]] += 1
            else:
                hash2[t[i]] = 1

        return hash1 == hash2



           


        
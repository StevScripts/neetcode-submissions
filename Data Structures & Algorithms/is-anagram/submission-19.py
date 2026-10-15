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
            hash1[s[i]] = 1 + hash1.get(s[i],0)
            hash2[t[i]] = 1 + hash2.get(t[i],0)


        return hash1 == hash2



           


        
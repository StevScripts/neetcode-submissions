class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = Counter(s)
        for i in range(len(s)):
            currentChar = t[i]
            if currentChar not in sCount:
                return False
            
            if sCount[currentChar] == 0:
                return False

            sCount[currentChar] -= 1
        
        return True
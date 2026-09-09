class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Check if the counter of both is the same
        #Nested loop
        #Get the counter val of the first item, then check if any others have the same counter val
        #return the string

        
        anagramsLen = len(strs)
        entireGroup = []

        for i in range(anagramsLen):
            currentAnagram = Counter(strs[i])
            currentList = []
            for j in range(anagramsLen):
                newAnagram = Counter(strs[j])
                if currentAnagram == newAnagram:
                    currentList.append(strs[j])
            if currentList not in entireGroup:
                entireGroup.append(currentList)

        return entireGroup
                 

        
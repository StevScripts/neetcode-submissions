class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        foundMax = -1
        temp = -1

        #Save cur val to temp
        #set arr[i] = foundMax
        #reset foundMax by comparing vals

        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = foundMax
            foundMax = max(foundMax,temp)
            
        return arr
                
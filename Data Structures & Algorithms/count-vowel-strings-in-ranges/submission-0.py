class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []


        vowels = {'a','e','i','o','u'}
        '''
        set of vowels

        loop through len queries,
            counter = 0
            for i in range(queries[0],queries[1]):

                if words[i][0] in vowels and words[i][-1] in vowels:
                    counter += 1
        
        '''

        for i in range(len(queries)):
            counter = 0

            for j in range(queries[i][0],queries[i][1]+1):
                if words[j][0] in vowels and words[j][-1] in vowels:
                    counter += 1
            ans.append(counter)

        return ans
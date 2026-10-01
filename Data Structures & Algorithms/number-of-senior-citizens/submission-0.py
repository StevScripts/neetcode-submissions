class Solution:
    def countSeniors(self, details: List[str]) -> int:
        '''
        10 - phone num
        next char - gender
        2 -age
        2 - seat
        '''

        tot = 0
        for i in range(len(details)):
            s = details[i][11] + details[i][12]
            
            if int(s) > 60:
                tot += 1

        return tot
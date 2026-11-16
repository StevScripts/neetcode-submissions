class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)




    def decode(self, s: str) -> List[str]:
        curPos = 0
        retList = []

        while curPos < len(s):
            lenStart,lenEnd = curPos,curPos
            while s[lenEnd] != '#':
                lenEnd += 1
            strLen = int(s[lenStart:lenEnd])
            curPos = lenEnd+1

            newString = s[curPos:curPos+strLen]
            curPos = curPos+strLen
            
            retList.append(newString)

        return retList

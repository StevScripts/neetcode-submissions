class Solution:
    def isValid(self, s: str) -> bool:
        sLen = len(s)
        if sLen == 0:
            return False

        stack = []

        for i in range(sLen):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if not stack:
                    return False
                
                poppedItem = stack.pop()
                if poppedItem != '(' and s[i] == ')':
                    return False
                if poppedItem != '{' and s[i] == '}':
                    return False
                if poppedItem != '[' and s[i] == ']':
                    return False
                
        if not stack:
            return True

        return False

            
        
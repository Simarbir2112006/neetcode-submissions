class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        pairs = {
            ']':'[',
            ')':'(',
            '}':'{'
            }
        
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c in pairs:
                if len(stack) != 0 and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) > 0:
            return False

        return True

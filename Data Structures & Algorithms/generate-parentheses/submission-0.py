class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(curr, o, c):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return
            
            if o < n:
                curr.append("(")
                backtrack(curr, o + 1, c)
                curr.pop()
            
            if c < o:
                curr.append(")")
                backtrack(curr, o, c + 1)
                curr.pop()
        
        backtrack([], 0, 0)
        return res
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        n = len(digits)
        res = []

        freq = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}

        def backtrack(i, curr):
            if i == n:
                res.append("".join(curr))
                return
            
            for j in freq[digits[i]]:
                curr.append(j)
                backtrack(i + 1, curr)
                curr.pop()
                
        backtrack(0, [])

        return res
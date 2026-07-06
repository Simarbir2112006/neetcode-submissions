class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = leng = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                leng -= 1
                l += 1
            
            window.add(s[r])
            leng += 1
            res = max(res, leng)
        
        return res
            
        
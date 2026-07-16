class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_words = s.split()
        
        return len(s_words[-1])
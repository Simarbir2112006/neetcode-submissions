class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_table = {}
        t_table = {}

        for i in range(len(s)):
            if s[i] in s_table:
                s_table[s[i]] += 1
            else:
                s_table[s[i]] = 1

            if t[i] in t_table:
                t_table[t[i]] += 1
            else:
                t_table[t[i]] = 1
        
        return s_table == t_table
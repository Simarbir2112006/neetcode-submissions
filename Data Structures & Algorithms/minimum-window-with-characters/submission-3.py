import string

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_freq = {}
        s_window = {}

        for i in t:
            t_freq[i] = 1 + t_freq.get(i, 0)

        l, r = 0, 0
        res = [-1, -1]
        res_len = float('inf')

        have, need = 0, len(t_freq)


        for r in range(len(s)):
            c = s[r]
            s_window[c] = 1 + s_window.get(c, 0)

            if c in t_freq and s_window[c] == t_freq[c]:
                have += 1

            while have >= need:
                if res_len > len(s[l:r + 1]):
                    res = [l,r]
                    res_len = (r - l + 1)
                s_window[s[l]] -= 1
                if s[l] in t_freq and s_window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""


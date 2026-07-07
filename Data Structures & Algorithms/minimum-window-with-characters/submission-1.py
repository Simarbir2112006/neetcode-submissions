class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = Counter(t)
        l, r = 0, 0
        res = ""

        while r < len(s):
            s_window = Counter(s[l:r + 1])

            if s_window >= t_freq:
                if res == "" or len(res) > len(s[l:r + 1]):
                    res = s[l:r + 1]
                l += 1
            else:
                r += 1
        
        return res


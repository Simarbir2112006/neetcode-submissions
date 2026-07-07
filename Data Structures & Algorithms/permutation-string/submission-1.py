class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1 = len(s1)
        n_s2 = len(s2)
        s1_freq = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 
            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
            }
        s2_window = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 
            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
            }

        for i in s1:
            s1_freq[i] += 1
        
        print(s1_freq)
    
        l = 0
        for r in range(n_s2):
            s2_window[s2[r]] += 1
            print(l, r)

            if (r - l + 1) > n_s1:
                s2_window[s2[l]] -= 1
                l += 1

            if (r - l + 1) == n_s1 and s1_freq == s2_window:
                return True
            
            print(s2_window)
        
        return False
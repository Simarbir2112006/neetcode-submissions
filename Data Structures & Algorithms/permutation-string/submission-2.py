class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1 = len(s1)
        n_s2 = len(s2)
        s1_freq = Counter(s1)

        l = 0
        for r in range(n_s2):
            if (r - l + 1) > n_s1:
                l += 1

            if (r - l + 1) == n_s1:
                s2_window = Counter(s2[l:r+1])
                if s1_freq == s2_window: 
                    return True
        
        return False
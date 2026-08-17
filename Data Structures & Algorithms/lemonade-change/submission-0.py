class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        have = {5: 0, 10: 0, 20: 0}

        for i in bills:
            have[i] += 1

            change = i - 5 # either 0 or 5 or 15
            
            if change == 0:
                continue
            
            elif change == 5:
                have[5] -= 1
            
            else:
                if have[10] > 0:
                    have[10] -= 1
                    have[5] -= 1
                else:
                    have[5] -= 3
            
            if have[5] < 0 or have[10]< 0:
                return False
        
        return True
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:        
        # finding peak
        l = 0
        n = mountainArr.length()
        r = n - 1
        
        while l <= r:
            m = (l + r) // 2

            if m < r and mountainArr.get(m) > mountainArr.get(m + 1):
                r = m

            elif m == r:
                break
            
            else:
                l = m + 1
        
        peak = m


        # search one half or peak and if not found then other half
        left_idx = -1

        if mountainArr.get(0) <= target:
            l = 0
            r = peak

            while l <= r:
                m = (l + r) // 2

                if target == mountainArr.get(m):
                    left_idx = m
                    break
                
                elif target > mountainArr.get(m):
                    l = m + 1
                
                else:
                    r = m - 1

        if left_idx != -1:
            return left_idx
        
        if mountainArr.get(n - 1) <= target:
            l = peak
            r = n - 1

            while l <= r:
                m = (l + r) // 2

                if target == mountainArr.get(m):
                    return m
                
                elif target < mountainArr.get(m):
                    l = m + 1
                
                else:
                    r = m - 1
        return -1
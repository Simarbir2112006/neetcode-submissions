class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

# it will traverse the piles and give me true if given rate works or false if time > h        
        def trying(k: int, h: int) -> bool: 
            time = 0
            for i in piles:
                time += math.ceil(i / k)

            return True if time <= h else False 
        
        
        l = 1
        r = max(piles)
        k = float('inf')
        while l <= r:
            m = (l + r) // 2

            if trying(m, h):
                r = m - 1
                k = min(m , k)
            
            else:
                l = m + 1
        
        return k
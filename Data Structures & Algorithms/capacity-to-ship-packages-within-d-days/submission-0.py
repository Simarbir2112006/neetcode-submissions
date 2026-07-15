class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def trying(max_weight): # true if max_weight and days work else false
            no_day = 1
            curr = 0
            for w in weights:
                if w + curr > max_weight:
                    no_day += 1
                    curr = w
                else:
                    curr += w
            
            return no_day <= days
        
        l = max(weights)
        r = sum(weights)
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2

            if trying(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res

        


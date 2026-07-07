class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 1
        res = float('inf')

        while r <= len(nums):
            total = sum(nums[l:r])
            print(total)
            if total >= target:
                res = min(res, (r-l))
                l += 1
            elif total < target:
                r+=1
            
            print(l, r)
        
        return res if res != float('inf') else 0
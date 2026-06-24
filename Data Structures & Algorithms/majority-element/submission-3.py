class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, max_count = 0, 0
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if count[i] > max_count:
                max_count = count[i]
                res = i
        
        return res
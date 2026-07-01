class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        res = 0
        prefixSum = [0] * (len(nums) + 1)

        for i in range(1, len(nums)+1):
            pref = nums[i-1] + prefixSum[i-1]
            prefixSum[i] = pref

            if (pref - k) in count:
                res+=count[pref-k]
            
            count[pref] = 1 + count.get(pref, 0)
        
        return res
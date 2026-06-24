class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        target = math.floor(len(nums)/3)

        for i in nums:
            count[i] = 1 + count.get(i, 0)

            if count[i] > target and i not in res:
                res.append(i)
        
        return res
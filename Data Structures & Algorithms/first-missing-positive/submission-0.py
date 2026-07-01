class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums_set = set(nums)

        while True:
            if res in nums_set:
                res+=1
            else:
                return res
        
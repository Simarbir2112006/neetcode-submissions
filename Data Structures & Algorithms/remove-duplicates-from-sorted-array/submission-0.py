class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        final = list(set(nums))
        final.sort()
        k = len(final)
        for i in range(k):
            nums[i] = final[i]
        
        return k
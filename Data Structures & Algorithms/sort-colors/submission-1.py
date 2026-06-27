class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rec = {0: 0, 1:0, 2:0}
        for i in nums:
            rec[i] += 1
        print(rec)
        zero, one, two = rec[0], rec[1], rec[2]
        one += zero

        nums[0:zero] = [0] * zero
        nums[zero:one] = [1] * (one - zero)
        nums[one:len(nums)] = [2] * two
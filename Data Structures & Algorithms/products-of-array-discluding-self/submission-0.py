class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)

        res = [0] * leng
        before = [0] * leng
        after = [0] * leng

        before[0] = 1
        after[-1] = 1

        for i in range(1, leng):
            before[i] = before[i-1] * nums[i-1]

        for i in range(leng-2, -1, -1):
            after[i] = after[i+1] * nums[i+1]
        
        for i in range(leng):
            res[i] = before[i] * after[i]
        
        return res
        
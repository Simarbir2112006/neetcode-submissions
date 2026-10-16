class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        arr = []
        def backtrack(i):
            if i >= len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[i])
            backtrack(i+1)

            arr.pop()
            backtrack(i+1)
        
        backtrack(0)
        
        return res

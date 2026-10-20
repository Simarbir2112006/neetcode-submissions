class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.add(tuple(subset.copy()))
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)

        return [list(s) for s in res]
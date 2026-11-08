class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k

        if total % k != 0:
            return False

        nums.sort(reverse=True)
        subsets = [0] * k

        def backtrack(i):
            if i >= len(nums):
                return True
            
            seen = set()

            for j in range(k):
                if subsets[j] in seen:
                    continue

                if subsets[j] + nums[i] <= target:
                    seen.add(subsets[j])
                    subsets[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    subsets[j] -= nums[i]
            
            return False
        
        return backtrack(0)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums_set:
            if i-1 not in nums_set:
                leng = 0
                while (i + leng) in nums_set:
                    leng+=1
                longest = leng if leng > longest else longest
        
        return longest
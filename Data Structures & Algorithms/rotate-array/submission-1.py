class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        split = n - k

        l = nums[:split]
        r = nums[split:]

        nums[:len(r)] = r
        nums[len(r):] = l
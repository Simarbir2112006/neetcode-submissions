class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        s = [] #[index,height]

        for i, h in enumerate(heights):
            start = i

            while s and s[-1][1] > h:
                idx, height = s.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            
            s.append([start, h])

        for i, h in s:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
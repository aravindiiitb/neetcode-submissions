class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        stack = []

        for i in range(len(heights) + 1):            
            while stack and (i == len(heights) or heights[i] <= heights[stack[-1]]):
                index = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, heights[index]*(width))

            stack.append(i)


        return maxArea
        
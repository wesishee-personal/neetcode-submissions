class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
        
        
        
        
        
        # for i in range(len(heights)):
        #     l, r = 1,1
        #     left_area, right_area = 0, 0
        #     while i-l >= 0:
        #         if heights[i-l] >= heights[i]:
        #             left_area += heights[i]
        #             l += 1
        #         else:
        #             break
        #     while i+r < len(heights):
        #         if heights[i+r] > heights[i]:
        #             right_area += heights[i]
        #             r += 1
        #         else:
        #             break
        #     current_area = heights[i] + left_area + right_area
        #     max_area = max(max_area, current_area)

        # return max_area


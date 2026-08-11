class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        max = 0
        while l < r:
            current_vol = min(heights[l],heights[r]) * (r-l)
            if current_vol > max:
                max = current_vol
            if heights[l] < heights[r]:
                l +=1
            else:
                r-=1
            # while r < len(heights):
            #     current_vol = min(heights[l],heights[r]) * (r-l)
            #     if current_vol > max:
            #         max = current_vol
            #     r+=1
            # l+=1
            # r = l+1
        return max
    
            
        

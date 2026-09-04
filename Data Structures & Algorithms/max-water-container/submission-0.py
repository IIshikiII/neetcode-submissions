class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) -1
        L_height = heights[L]
        R_height = heights[R]
        max_area = min(L_height, R_height) * (R - L)
        while L < R:
            if heights[L] <= heights[R]:
                L += 1
                if heights[L] > L_height:
                    L_height = heights[L]
                    new_area = min(L_height, R_height) * (R - L)
                    if new_area > max_area:
                        max_area = new_area 
            elif heights[L] > heights[R]:
                R -= 1
                if heights[R] > R_height:
                    R_height = heights[R]
                    new_area = min(L_height, R_height) * (R - L)
                    if new_area > max_area:
                        max_area = new_area 
        
        return max_area
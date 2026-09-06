class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # List[tuple[int, int]]
        for idx, val in enumerate(heights):
            poped_id = idx
            while len(stack) >= 1 and val < stack[-1][1]:
                poped_id, poped_val = stack.pop()
                area = poped_val * (idx - poped_id)
                if area > max_area:
                    max_area = area
            stack.append((poped_id, val))
        for val in stack:
            area = val[1] * (len(heights) - val[0])
            if area > max_area:
                max_area = area
        return max_area
class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        cumsum = 0
        L_height = height[L]
        R_height = height[R]
        while L < R:
            while (L_height <= R_height) and (L < R):
                L += 1
                if height[L] < L_height:
                    cumsum += L_height - height[L]
                    # print(L, R, cumsum)
                else:
                    L_height = height[L]

            while (L_height > R_height) and (L < R):
                R -= 1
                if height[R] < R_height:
                    cumsum += R_height - height[R]
                    # print(L, R, cumsum)
                else:
                    R_height = height[R]

        return cumsum

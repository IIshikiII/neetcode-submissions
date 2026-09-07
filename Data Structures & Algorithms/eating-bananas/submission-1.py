from math import ceil
class Solution:
    def count_time(self, piles: List[int], k: int) -> int:
        cumsum = 0
        for pile in piles:
            cumsum += ceil(pile / k)
        return cumsum

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2
            time = self.count_time(piles, mid_k)
            if time > h:
                min_k = mid_k + 1
            elif time <= h:
                max_k = mid_k - 1
    
        return min_k
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] <= nums[R]:
                return nums[L]
            if R - L == 1:
                return min(nums[L], nums[R])
            mid = (L + R) // 2
            if nums[mid] >= nums[L]:
                L = mid + 1
            elif nums[mid] < nums[L]:
                R = mid
        return nums[R]

class Solution:
    def bin_search(self, nums: list[int], target: int, L: int, R: int) -> int:
        L = L
        R = R
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        return -1

    def findMin(self, nums: List[int]) -> int:
        
        L = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] <= nums[R]:
                return L
            if R - L == 1:
                if nums[L] <= nums[R]:
                    return L
                else:
                    return R
            mid = (L + R) // 2
            if nums[mid] >= nums[L]:
                L = mid + 1
            elif nums[mid] < nums[L]:
                R = mid
        return R
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        shift = self.findMin(nums=nums)
        if shift > 0:
            L1 = 0
            R1 = shift -1
            L2 = shift
            R2 = n -1
            res1 = self.bin_search(nums, target, L1, R1)
            res2 = self.bin_search(nums, target, L2, R2)
            if max(res1, res2) >= 0:
                return max(res1, res2)
            else:
                return -1
        else:
            return self.bin_search(nums, target, 0, n - 1)



        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for elem in nums:
            if elem not in nums_set:
                nums_set.add(elem)
            else:
                return True
        return False
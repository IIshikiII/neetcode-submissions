class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = 1 + nums_dict.get(num, 0)
        
        return sorted(nums_dict, key=nums_dict.get, reverse=True)[: k]
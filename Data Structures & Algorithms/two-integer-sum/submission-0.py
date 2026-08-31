class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_count = {}
        for elem in nums:
            nums_count[elem] = 1 + nums_count.get(elem, 0)

        for num in nums_count:
            if target -  num == num:
                if nums_count[num] >= 2:
                    equal_values = True
                    res_num = num
            elif target -  num in nums_count:
                equal_values = False
                res_num = num

        if equal_values == True:
            idx1 = nums.index(res_num)
            idx2 = idx1 + nums[idx1 + 1:].index(res_num) + 1
        else:
            idx1 = nums.index(res_num)
            idx2 = nums.index(target - res_num)

        return [idx1, idx2] if idx1 < idx2 else [idx2, idx1]

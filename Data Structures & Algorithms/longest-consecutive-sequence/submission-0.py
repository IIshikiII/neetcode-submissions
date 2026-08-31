class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_length = 0
        while nums_set:
            number = nums_set.pop()
            curr_seq_length = 1
            i = 1
            while number - i in nums_set:
                curr_seq_length += 1
                nums_set.remove(number - i)
                i += 1
            i = 1
            while number + i in nums_set:
                curr_seq_length += 1
                nums_set.remove(number + i)
                i += 1
            if curr_seq_length > max_length:
                max_length = curr_seq_length
        return max_length
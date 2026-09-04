class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for idx, number in enumerate(nums):
            if idx < len(nums):
                L = 0
                R = len(nums) - 1
                vals = []
                while L < R:
                    if L == idx:
                        L += 1
                        continue
                    elif R == idx:
                        R -= 1
                        continue
                    # print(f"number {number}")
                    # print(f"L: {L}", f"R: {R}", f"nums[L]: {nums[L]}", f"nums[R]: {nums[R]}", f"nums[L] + nums[R]: {nums[L] + nums[R]}", -number, sep=" | ")
                    if nums[L] + nums[R] > -number:
                        R -= 1
                    elif nums[L] + nums[R] < -number:
                        L += 1
                    else:
                        vals.append([number, nums[L], nums[R]])
                        R -= 1

                for val in vals:
                    exists_flag = False
                    for lst in res:
                        if set(val) == set(lst):
                            exists_flag = True
                            break
                    if exists_flag:
                        continue
                    else:
                        res.append(val)
        return res

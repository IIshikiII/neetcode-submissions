class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod_list = [None] * n
        postfitx_prod_list = [None] * n
        result_list = [None] * n
        
        for i in range(n):
            if i == 0:
                prefix_prod_list[i] = nums[i]
                postfitx_prod_list[n - 1 - i] = nums[n - 1 - i]
            else:
                prefix_prod_list[i] = nums[i] * prefix_prod_list[i-1]
                postfitx_prod_list[n - 1 - i] = nums[n - 1 - i] * postfitx_prod_list[n- i]
                
        for i in range(n):
            if i == 0:
                result_list[i] = postfitx_prod_list[i + 1]
            elif i == n - 1:
                result_list[i] = prefix_prod_list[i - 1]
            else:
                result_list[i] = prefix_prod_list[i - 1] * postfitx_prod_list[i + 1]

        return result_list
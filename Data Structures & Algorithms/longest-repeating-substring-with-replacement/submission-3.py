class Solution:
    def validRange(self, counts: Dict, L: int, R: int, k: int) -> bool:
        if not counts:
            return True
        max_char = max(counts, key=lambda x: counts[x])
        return (R - L + 1) - counts[max_char] <= k
    
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0

        nums_dict = {}
        max_length = 0
        L = 0
        R = 0
        for R in range(len(s)):
            nums_dict[s[R]] = nums_dict.get(s[R], 0) + 1
            while not self.validRange(nums_dict, L, R, k):
                nums_dict[s[L]] -= 1
                L += 1
            max_length = max(max_length, R - L + 1)

        return max_length
            

        



        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        L = 0
        max_len = 0
        nums_set = set()
        
        for R in range(len(s)):
            if s[R] not in nums_set:
                nums_set.add(s[R])
            else:
                max_len = max(max_len, R - L)
                while s[R] in nums_set:
                    nums_set.remove(s[L])
                    L += 1
                nums_set.add(s[R])
        max_len = max(max_len, R - L + 1)
        return max_len
            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        brackets = {"(": ")", "{": "}", "[": "]"}
        while i < len(s):
            if s[i] in brackets.keys():
                stack.append(s[i])
            else:
                if len(stack) >= 1 and s[i] == brackets[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
            i += 1
        if stack:
            return False
        return True

        
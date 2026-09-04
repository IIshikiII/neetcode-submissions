import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_chars = string.ascii_letters + string.digits
        L = 0
        R = len(s) - 1

        while L <= R:
            while not s[L].isalnum():
                if L + 1 < len(s):
                    L += 1
                else:
                    return True
            while not s[R].isalnum():
                if  R - 1 >= 0:
                    R -= 1

            
            if s[L].lower() != s[R].lower():
                print(s[L].lower(), s[R].lower())
                return False
            L += 1
            R -= 1

        return True


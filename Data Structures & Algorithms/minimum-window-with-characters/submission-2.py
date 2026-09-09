class Solution:
    def flag(self, hash_table: Dict) -> bool:
        for value in hash_table.values():
            if value > 0:
                return True
        return False

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        hash_table = {}
        for char in t:
            hash_table[char] = hash_table.get(char, 0) + 1
        
        L = 0
        R = len(t) - 1
        min_str_len = len(s) + 1
        min_str = ""
        valid_str = s * 2
        for i in range(0, len(t)):
            if s[i] in hash_table:
                hash_table[s[i]] -= 1
        
        while R < len(s):
            while self.flag(hash_table):
                R += 1
                if R == len(s):
                    break
                if s[R] in hash_table:
                    hash_table[s[R]] -= 1
            if not self.flag(hash_table):
                while not self.flag(hash_table):
                    L += 1
                    if s[L - 1] in hash_table:
                        hash_table[s[L - 1]] += 1
                valid_str = s[L-1:R+1]
                if len(valid_str) < min_str_len:
                    min_str_len = len(valid_str)
                    min_str = valid_str


        return min_str    
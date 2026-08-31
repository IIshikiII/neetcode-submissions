class Solution:
    def hash_key(self, s: str) -> str:
        char_counts = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
        }
        for i in range(len(s)):
            char_counts[s[i]] += 1
        hash_str = ""
        for char, count in char_counts.items():
            hash_str += f"{char}{count}"
        return hash_str
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}
        for elem in strs:
            hash_count = self.hash_key(elem)
            if hash_count not in dict_strs:
                dict_strs[hash_count] = [elem]
            else:
                dict_strs[hash_count].append(elem)
        
        return list(dict_strs.values())
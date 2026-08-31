class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res_str = ""
        for string in strs:
            res_str += f"{str(len(string))}#{string}"
        return res_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        res = []
        mode = "reading_len"
        while i < len(s):
            if mode == "reading_len":
                j = 0
                len_str = ""
                while s[i+j] != "#":
                    len_str += s[i]
                    i += 1
                    continue
                else:
                    len_str = int(len_str)
                    mode = "reading_str"
                    i += 1
                    if len_str == 0:
                        res.append("")
                        mode = "reading_len"
                
            elif mode == "reading_str":
                string = s[i:i+len_str]
                res.append(string)
                mode = "reading_len"
                i += len_str
    
        return res
            


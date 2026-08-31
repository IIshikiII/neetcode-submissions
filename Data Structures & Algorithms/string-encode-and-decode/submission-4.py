class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        splitter = str(strs[0].__hash__())
        return f"{len(splitter)}e{splitter}" + splitter.join(strs)
    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        splitter_length = ""
        for elem in s:
            if elem == "e":
                break
            splitter_length += elem
        n = len(splitter_length)
        splitter_length = int(splitter_length)
        splitter = s[n+1:splitter_length+n+1]
        return s.split(splitter)[1:]
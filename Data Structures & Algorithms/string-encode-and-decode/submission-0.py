class Solution:
    def encode(self, strs: List[str]) -> str:
        token = "<CAT>" 
        s = "" 
        for string in strs: 
            s += string; s += token
        return s
    def decode(self, s: str) -> List[str]:
        return s.split("<CAT>")[:-1]

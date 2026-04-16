class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return "None"
        result = '@@'.join(strs)
        return result
    def decode(self, s: str) -> List[str]:
        if s == "None": return []
        result = s.split('@@')
        return result
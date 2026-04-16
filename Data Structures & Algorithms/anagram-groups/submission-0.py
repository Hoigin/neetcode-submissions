class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = list(set(''.join(sorted(s)) for s in strs))
        output_strs = []
        for sorted_s in sorted_strs:
            temp = [s for s in strs if ''.join(sorted(s))==sorted_s]
            output_strs.append(temp)
        return output_strs
            
                
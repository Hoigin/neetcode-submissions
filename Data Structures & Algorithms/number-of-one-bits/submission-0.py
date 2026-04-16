class Solution:
    def hammingWeight(self, n: int) -> int:
        nbin = f"{n:b}"
        count = Counter(list(nbin))
        return count['1']
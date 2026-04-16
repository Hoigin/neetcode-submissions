class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            perms = []
            insert_pts = len(res[0])+1
            for p in res:
                for j in range(insert_pts):
                    pcopy = p.copy()
                    pcopy.insert(j, n)
                    perms.append(pcopy)
            res = perms
        return res
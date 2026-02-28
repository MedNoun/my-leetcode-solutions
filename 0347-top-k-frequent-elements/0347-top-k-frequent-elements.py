class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n,0) + 1
        b_sort = [[] for _ in range(len(nums) + 1)]
        for ky,v in occ.items():
            b_sort[v].append(ky)
        i = len(nums)
        res = []
        while k>0:
            while len(b_sort[i]) == 0:
                i -=1
            res.append(b_sort[i].pop())
            k-=1
        return res
        
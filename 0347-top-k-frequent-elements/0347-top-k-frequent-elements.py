class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for el in nums:
            try:
                occ[el] += 1
            except:
                occ[el] = 1
        sort = sorted(occ.items(), key=lambda x: x[1], reverse= True)
        return [sort[i][0] for i in range(k)]
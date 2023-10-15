import heapq
class Solution:
    def topKFrequent(self, nums, k):
        out = {}
        for num in nums:
            try:
                out[num]+=1
            except:
                out[num]= 1
        pq = []
        for el in out:
            heapq.heappush(pq,(out[el],el))
            if len(pq)>k: heappop(pq)
        return [i[1] for i in pq]
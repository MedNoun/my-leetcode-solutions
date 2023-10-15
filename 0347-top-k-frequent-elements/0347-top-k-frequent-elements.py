class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        table = {}
        prev = None
        for num in nums:
            table[num] = table.get(num,0) + 1
        r = sorted(table.items(),key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(r[i][0])
        return result
                
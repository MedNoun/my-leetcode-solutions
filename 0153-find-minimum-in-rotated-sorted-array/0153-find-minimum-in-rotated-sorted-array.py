class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 1
        last = len(nums)
        result = nums[0]
        i = 0
        while first <= last and i<1000:
            i+=1
            k = (last - first)//2 + first
            candidate = nums[-k]
            print(first, last, k, candidate)
            if candidate < result:
                first = k+1
                result = candidate
            else:
                last = k-1
        return result
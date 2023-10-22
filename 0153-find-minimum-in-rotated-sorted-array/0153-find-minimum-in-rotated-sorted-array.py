class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 1
        last = len(nums)
        result = nums[0]
        while first <= last:
            k = (last - first)//2 + first
            candidate = nums[-k]
            if candidate < result:
                first = k+1
                result = candidate
            else:
                last = k-1
        return result
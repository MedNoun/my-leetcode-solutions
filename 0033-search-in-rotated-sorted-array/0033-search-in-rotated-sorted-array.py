class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin() -> int:
            first = 1
            last = len(nums)
            result = 0
            while first <= last:
                k = (last - first)//2 + first
                candidate = -k
                if nums[candidate] < nums[result]:
                    first = k+1
                    result = candidate
                else:
                    last = k-1
            return result
        l = findMin()
        r = l + len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m]<target:
                l = m+1
            elif nums[m]>target:
                r = m-1
            else:
                return (m+len(nums))%len(nums)
        return -1


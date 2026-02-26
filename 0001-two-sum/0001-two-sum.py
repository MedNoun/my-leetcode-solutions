class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t_val = {}
        for i in range(len(nums)):
            j = t_val.get(target - nums[i], None)
            if j != None :
                return [i, j]
            t_val[nums[i]] = i
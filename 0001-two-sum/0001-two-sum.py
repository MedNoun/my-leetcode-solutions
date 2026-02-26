class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_nums = [{"i" : k, "v" : nums[k]} for k in range(len(nums))]
        nums = sorted(dic_nums, key=lambda x : x.get("v"))
        i , j = 0 , len(nums) - 1
        while i<j:
            s = nums[i]["v"] + nums[j]["v"]
            if s == target:
                return [nums[i]["i"],nums[j]["i"]]
            if s < target:
                i+=1
            if s > target:
                j-=1
        return []
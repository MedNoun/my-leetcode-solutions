class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_array = sorted(enumerate(nums),key=lambda x:x[1])
        i = 0
        j = len(sorted_array) - 1
        while(True):
            somme = sorted_array[i][1] + sorted_array[j][1]
            if somme == target:
                return [sorted_array[i][0], sorted_array[j][0]]
            if somme > target:
                j = j-1
            else:
                i = i+1
       
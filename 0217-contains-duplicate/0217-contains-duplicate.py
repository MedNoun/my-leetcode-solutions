class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for el in nums:
            dic[el] = 0
        for el in nums:
            dic[el] += 1
            if(dic[el] == 2): return True
        return False
            
        
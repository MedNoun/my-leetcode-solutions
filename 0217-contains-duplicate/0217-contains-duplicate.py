class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for el in nums:
            try:
                dic[el] += 1
                if(dic[el] == 2): return True
            except:
                dic[el] = 1
        return False
            
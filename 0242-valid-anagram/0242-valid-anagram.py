class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in t:
            try:
                chars[char] +=1
            except:
                chars[char] = 1
        for char in s:
            try:
                chars[char] -=1
            except:
                return False
        for el in chars:
            if chars[el]!=0: return False
        return True
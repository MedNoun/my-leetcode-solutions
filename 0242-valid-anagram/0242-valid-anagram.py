class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            res[ord(s[i]) - 97] += 1
            res[ord(t[i]) - 97] -= 1
        for v in res:
            if v != 0 :
                return False
        return True

        
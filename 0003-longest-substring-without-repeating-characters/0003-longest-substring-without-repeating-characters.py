class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p2 = 0
        p1 = 0
        maxi = 0
        occ = {}
        while p2<len(s):
            if occ.get(s[p2]):
                maxi = max(maxi, p2 - p1)
                while True :
                    if s[p1] == s[p2]:
                        p1+=1
                        break
                    occ[s[p1]] = 0
                    p1 += 1
            
            occ[s[p2]] = 1    
            p2 += 1

        return max(maxi, p2 - p1)
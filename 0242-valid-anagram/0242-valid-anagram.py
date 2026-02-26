class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem = {}
        for c in s:
            mem[c] = mem.get(c, 0) + 1
        for c in t:
            if not mem.get(c, None):
                return False
            mem[c]-=1
        occ = set(mem.values())
        return len(occ)==1 and 0 in occ

        
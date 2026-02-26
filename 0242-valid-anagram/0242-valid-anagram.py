class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,  97, 101]
        s_hash = 1
        t_hash = 1
        for i in range(min(len(s), len(t))):
            s_hash *= primes[ord(s[i]) - 97]
            t_hash *= primes[ord(t[i]) - 97]

        return s_hash == t_hash and len(s) == len(t)

        
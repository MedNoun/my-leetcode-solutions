PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def prime(c):
            return PRIMES[ord(c) - ord('a')]
        if len(s2)<len(s1):
            return False
        h = 1
        h_c = 1
        for i in range(len(s1)):
            h*=prime(s1[i])
            h_c*=prime(s2[i])
        i = 0
        j = len(s1) - 1
        while j<len(s2)-1 and h_c!=h:
            j+=1
            h_c=h_c*prime(s2[j])//prime(s2[i])
            i+=1
        return h_c == h
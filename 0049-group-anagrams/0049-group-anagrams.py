PRIMES=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for s in strs:
            m = 1
            for l in s:
                prime = PRIMES[ord(l) - ord("a")]
                m *= prime
            ht[m] = ht.get(m,[]) + [s]
        result = []
        for v in ht.values():
            result.append(v)
        return result

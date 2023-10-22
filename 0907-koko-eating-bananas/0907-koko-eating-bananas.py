from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def neededTime(k):
            t = 0
            for p in piles:
                t += ceil(p/k)
                if t>h:
                    return t
            print("needed time for {} is {}".format(k,t))
            return t
        start = ceil(sum(piles)/h)
        finish = max(piles)
        results = []
        i = 0
        while finish!=start and i<1000:
            i+=1
            k = (finish - start)//2 + start
            t = neededTime(k)
            if t>h:
                start = max(start + 1, k)
            elif t<h:
                finish = min(finish - 1,k)
            else:
                finish = k
        return start


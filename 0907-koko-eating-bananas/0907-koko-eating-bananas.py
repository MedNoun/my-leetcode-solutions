from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def neededTime(k):
            t = 0
            for p in piles:
                t += ceil(p/k)
                if t>h:
                    return t
            return t
        start = ceil(sum(piles)/h)
        finish = max(piles)
        while finish!=start:
            k = (finish - start)//2 + start
            t = neededTime(k)
            if t>h:
                start = max(start + 1, k)
            elif t<h:
                finish = min(finish - 1,k)
            else:
                finish = k
        return start


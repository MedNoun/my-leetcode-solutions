class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = 0
        tuples = sorted(zip(position,speed),key=lambda x: x[0])
        while position:
            fleet1 = tuples.pop()
            if not tuples :
                n+=1
                break
            fleet2 = tuples.pop()
            t1 = (target - fleet1[0])/fleet1[1]
            t2 = (target - fleet2[0])/fleet2[1]
            if t2<=t1:
                tuples.append(fleet1)
            else:
                tuples.append(fleet2)
                n+=1
        return n
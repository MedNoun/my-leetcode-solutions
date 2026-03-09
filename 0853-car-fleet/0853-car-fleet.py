class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p, s in zip(position, speed)]
        stack = []
        for p in sorted(pairs)[::-1]:
            stack.append(p)
            if len(stack)>=2:
                c2, c1 = stack[-1], stack[-2]
                t1 = (target - c1[0]) / c1[1]
                t2 = (target - c2[0]) / c2[1]
                if t2 <= t1:
                    stack.pop()
        return len(stack)

        
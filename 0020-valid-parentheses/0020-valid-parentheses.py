class Solution:
    def isValid(self, s: str) -> bool:
        # filo
        maps = {"]" : "[", ")" : "(", "}": "{"}
        stack = []
        for c in s:
            if c in maps.values():
                stack.append(c)
            else :
                if len(stack) == 0 or stack.pop() != maps[c]:
                    return False
        return len(stack) == 0
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def solve(o,c):
            if o == c == n:
                result.append("".join(stack))
                return
            if o<n:
                stack.append("(")
                solve(o+1,c)
                stack.pop()
            if c < o:
                stack.append(")")
                solve(o,c+1)
                stack.pop()
        solve(0,0)
        return result
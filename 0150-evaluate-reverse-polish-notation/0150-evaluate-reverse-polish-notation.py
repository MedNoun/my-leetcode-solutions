class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            if token.isnumeric() or (token[0] == "-" and len(token)>1):
                numbers.append(token)
            else:
                right = numbers.pop()
                left = numbers.pop()
                numbers.append(str(int(eval(left + token + right))))
        return int(numbers.pop())
        
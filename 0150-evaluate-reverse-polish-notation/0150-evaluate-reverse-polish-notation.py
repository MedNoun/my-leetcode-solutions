class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ("+", "-", "*", "/")
        r = []
        i = 0

        while i < len(tokens) :

            while i < len(tokens) and tokens[i] not in ops:
                r.append(int(tokens[i]))
                i += 1

            if i < len(tokens) :
                b, a = r.pop(), r.pop()
                match tokens[i]:

                    case "+": r.append(a + b)
                    case "-": r.append(a - b)
                    case "*": r.append(a * b)
                    case "/": r.append(int(a / b))

                i+=1
        return r.pop()
                
        
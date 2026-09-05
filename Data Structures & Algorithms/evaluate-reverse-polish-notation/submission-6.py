class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "*", "-", "/"}

        i = 0
        while i < len(tokens):
            # print(stack, tokens[i])
            token = tokens[i]
            if token.isdigit():
                stack.append(token)
                i += 1
                continue
            elif len(token) > 1 and token[1:].isdigit():
                stack.append(token)
                i += 1
                continue
            elif token in operations:
                if token == "+":
                    res = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack[-1] = res
                elif token == "*":
                    res = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack[-1] = res
                elif token == "-":
                    res = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack[-1] = res
                elif token == "/":
                    res = int(stack[-2]) / int(stack[-1])
                    stack.pop()
                    stack[-1] = res
            i += 1
        return int(stack[0])
                    
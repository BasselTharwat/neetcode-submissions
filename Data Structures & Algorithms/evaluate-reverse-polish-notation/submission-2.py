class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        stack = []
        while i < len(tokens):
            if tokens[i] == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) + int(second))
                
            elif tokens[i] == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) - int(second))

            elif tokens[i] == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) * int(second))
            
            elif tokens[i] == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) / int(second))
            else:
                stack.append(tokens[i])
            
            print(i , stack)
            i += 1


        return int(stack[0])
        
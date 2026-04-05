class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        print(tokens)

        for i in range(len(tokens)):
            print(stack)
            if tokens[i] not in "+*/-":
                stack.append(tokens[i])
            else:
                right = stack.pop()
                left = stack.pop()
                print(left)
                print(right)
                if tokens[i] == "+":
                    res = str(int(int(left) + int(right)))
                elif tokens[i] == "-":
                    res = str(int(int(left) - int(right)))
                elif tokens[i] == "*":
                    res = str(int(int(left) * int(right)))
                elif tokens[i] == "/":
                    res = str(int(int(left) / int(right)))

                stack.append(res)

        return int(stack[0])
        
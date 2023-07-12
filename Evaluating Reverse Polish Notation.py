class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        oper = {"+","*","-","/"}
        for n in tokens:
            if n not in oper:
                stack.append(int(n))

            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
        
                if n == "+":
                    result = operand1 + operand2
                elif n == "*":
                    result = operand1 * operand2
                elif n == "/":

                    result = int(operand2 / operand1)
                else:
                    result = operand2 - operand1
                stack.append(result)
            
        return stack[0]

solution = Solution()
tokens = ['2','1','+','3','*']
reverse_polish = solution.evalRPN(tokens)
print(reverse_polish)

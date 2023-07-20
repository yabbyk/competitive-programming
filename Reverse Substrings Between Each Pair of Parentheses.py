class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
                
            elif i == ")":
                temp = []
                while stack[-1] != "(":

                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(i)
        return "".join(stack)
       


solution = Solution()
s = "(abcd)"
reverse = solution.reverseParentheses(s)
print(reverse)

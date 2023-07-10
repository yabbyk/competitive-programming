class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_pairs = {'(':')' , '[' :']' , '{':'}'}
        for chrs in s:
            if chrs in matching_pairs:
                stack.append(chrs)
            elif chrs in matching_pairs.values():
                
                if matching_pairs[stack.pop()] == chrs :
                    return True
                else:
                    return False

                    
        return len(stack)== 0

        

solution = Solution()
s = "()"
valid = solution.isValid(s)
print(valid)

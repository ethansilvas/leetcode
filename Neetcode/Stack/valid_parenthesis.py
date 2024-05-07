"""
use a stack to load all of our opening parenthesis 

if we run into a closing character we need to check: 
    stack is not empty
    equal to the top value of stack

then by the end of the loop we make sure the stack is empty
meaning that all the opening parenthesis have been closed
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False

        closings = {')': '(', ']': '[', '}': '{'}

        stack = []

        for char in s:
            if char in closings:
                if stack and stack[-1] == closings[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

        
        
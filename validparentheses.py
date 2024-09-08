class Solution:
    def isValid(self, s: str) -> bool:
        # initial variables
        n = len(s)
        stack = []
        hashtable = {
            '}': '{', 
            ']': '[',
            ')': '('
        }
        openers = ['(', '[','{']
        closers = [')', ']', '}']
        
        # core logic
        """
        We iterate over the characters one by one.
        Every opening bracket is pushed onto the stack.
        For every closing bracket, we check for the presence of a previous opening bracket
        If present, we pop it off the stack. 
        A pop represents a pair of opening and closing bracket.
        """

        for character in s:
            if character in openers: # if character is a opening bracket
                stack.append(character)
            else: # if character is a closing bracket
                if len(stack) == 0:
                    # if the stack is empty, there is no corresponding opener. 
                    # hence invalid string
                    return False 

                correspondingOpener = hashtable[character]
                stackTop = stack[-1]
                if stackTop == correspondingOpener:
                    stack.pop()
                else:
                    return False

        ## if there are some opening brackets without a matching closing bracket,
        # then the stack is not empty. Thus, invalid parentheses

        ## if all pairs of opening and closing brackets are cancelled out, 
        # the stack will be empty. valid parentheses
        if len(stack) == 0:
            return True
        else:
            return False

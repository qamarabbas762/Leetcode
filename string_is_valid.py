class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_dict = {'}':'{',')':'(',']':'[' }

        for i in s:
            if i not in bracket_dict:
                stack.append(i)
            elif stack!=[]:
                if stack[-1] ==bracket_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if stack ==[]:
            return True
        else:
            return False


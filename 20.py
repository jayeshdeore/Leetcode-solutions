# Valid Parenthesis

# Usually problems like this can be solved pretty easily with the help of a stack

bracket_dict = {')': '(', ']': '[', '}': '{'}

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s:
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            elif len(stack) > 0 and bracket_dict[bracket] == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.isValid('()()()[()]'))

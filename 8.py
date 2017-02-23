# ATOI


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        negative_flag = False
        str = str.strip()

        if str.startswith('-') or str.startswith('+'):
            if str.startswith('-'):
                negative_flag = True
                str = str[1:]
            else:
                str = str[1:]

        if len(str) == 0:
            return 0

        for x in range(len(str)):
            if not str[x] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                x -= 1
                break

        if x == -1:
            return 0
        else:
            number = int(str[:x + 1])
            if negative_flag is True:
                number *= -1

            if number > 2147483647:
                return 2147483647
            if number < -2147483648:
                return -2147483648
            return number


# Using regex
import re
pattern = re.compile('\s*([+-]?\d*)')

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        match = re.match(pattern, str)
        if not match:
            return 0
        else:
            try:
                number = int(match.groups(0)[0])
                if number > 2147483647:
                    return 2147483647
                if number < -2147483648:
                    return -2147483648
                return number
            except:
                return 0


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.myAtoi('-123545'))

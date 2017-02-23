# Palindrome number

# This does it using extra space by converting int to string and then validating whether the reversed string is same as actual
# But we need to do it without using any extra space


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            if x == int(str(x)[::-1]):
                return True
            else:
                return False


# Without using any extra space
class Solution(object):
    def isPalindrome(self, x):
        """
        First find number of digits in the number
        """
        if x < 0:
            return False
        else:
            divisor = 1
            division = 1
            while division is not 0:
                division = x // divisor
                divisor *= 10

        # Now we got the number of digits in the number, use the same variable
        # to save extra space
        division = 10
        divisor /= 100

        while division <= divisor:
            if (x % division) // (division / 10) != (x // divisor) % (division):
                return False
            x = x - (x // divisor) * divisor
            division *= 10
            divisor /= 10

        return True


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.isPalindrome(34543))

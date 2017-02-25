# Reverse 32 bit integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Find range of 32 bit integer
        lower_bound = -2**31
        upper_bound = lower_bound * (-1) + 1

        if x < 0:
            answer = -1 * self.reverse_string(-1 * x)
        else:
            answer = self.reverse_string(x)

        if answer > upper_bound or answer < lower_bound:
            return 0
        else:
            return answer

    def reverse_string(self, x):
        x = str(x)
        return int(x[::-1])


# Another beautiful implementation of the reverse without using any extra space, but since in python
# the length of an integer is not limited we need to have a separate case to take case of overflow.
class Solution(object):
    def reverse(self, x):
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10

        return rev


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.reverse(1234))


# If we use libraries like numpy, then we can do this faster
# Another way could be we first check size of number string and if size is equal to size of 2^31 only then we do the comparison
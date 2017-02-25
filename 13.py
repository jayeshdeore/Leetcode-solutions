# Roman to Integer, number lies in 1 to 3999


roman_values = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        for x in range(len(s) - 1):
            if roman_values[s[x]] < roman_values[s[x + 1]]:
                number = number - roman_values[s[x]]
            else:
                number += roman_values[s[x]]

        number += roman_values[s[-1]]
        return number


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.romanToInt('XVII'))

# The essence being if the next numeral in roman is bigger than current one then we need to substract that value else add that value to number
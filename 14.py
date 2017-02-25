# Longest common prefix among a list of strings

# We just traverse through all the forst elements of the string and ensure that the same element is present in each of the strings at the start
# The order in worst case would be O(mn), where n is number of strings and m is length of smallest string
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        index = 0
        try:
            while True:
                char = strs[0][index]
                for x in strs:
                    if x[index] != char:
                        return prefix
                index += 1
                prefix += char
        except:
            return prefix


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.longestCommonPrefix(['aabasdkjgfdnf', 'aabasdthf', 'aabasyht', 'aabasdtlttklrlgkrklg']))

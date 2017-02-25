# Find needle in haystack in a string

# We are using python find function directly, we can also implement a
# simple n^2 search for finding the pattern or use KMP to get it done in
# O(n), or we can use Robin Karp algo

# Have a look at python's find function, maybe it might be using a combination of above algos depending on use case


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.strStr('asdasddfgkkln', 'ddfg'))
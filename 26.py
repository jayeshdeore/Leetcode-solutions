# Remove Duplicate integers from a sorted array


# This will be of O(n)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        counter = 1
        for x in range(len(nums) - 1):
            if nums[x] != nums[x + 1]:
                nums[counter] = nums[x + 1]
                counter += 1

        return counter


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.removeDuplicates([1, 1, 2, 3, 3, 3, 4]))

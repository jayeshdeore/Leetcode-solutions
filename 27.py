# Remove all instances of a given element from an array and return it

# This should ne of O(n) with no extra memory for another array space O(1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        for x in range(len(nums)):
            if nums[x] == val:
                continue
            else:
                nums[counter] = nums[x]
                counter += 1

        return counter


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.removeElement([1, 1, 2, 3, 3, 3, 4], 2))

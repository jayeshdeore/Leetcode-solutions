# TWO SUM

# Solution 1: Brute force, O(n^2), space O(1)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]


# Solution 2: O(nlogn), space O(n)
class Solution(object):
    def twoSum(self, nums, target):
        nums_with_indexes = zip(nums, range(len(nums)))
        nums_with_indexes = sorted(nums_with_indexes)

        pointer1 = 0
        pointer2 = len(nums) - 1

        while pointer1 != pointer2:
            if nums_with_indexes[pointer1][0] + nums_with_indexes[pointer2][0] > target:
                pointer2 -= 1
            elif nums_with_indexes[pointer1][0] + nums_with_indexes[pointer2][0] < target:
                pointer1 += 1
            else:
                return [nums_with_indexes[pointer1][1], nums_with_indexes[pointer2][1]]


# Solution 3: hashmap, O(n), space O(n)
class Solution(object):
    def twoSum(self, nums, target):
        nums_dict  = {}
        for index in range(len(nums)):
            if target - nums[index] in nums_dict:
                return [nums_dict[target - nums[index]], index]
            else:
                nums_dict[nums[index]] = index

if __name__ == '__main__':
    my_class = Solution()
    print(my_class.twoSum([4,2,1], 5))

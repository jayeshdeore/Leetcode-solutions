# Median of two sorted arrays

# Order O(log(m+n))


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Check whether there are odd or even numbers in total
        if len(nums1) + len(nums2) % 2 == 1:
            pass

        l1 = len(nums1)
        l2 = len(nums2)

        while True:
            if x1 % 2 == 0:

                # We can also use recursion to get the median easily as well

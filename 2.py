# Add Two numbers

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# This will be roughly of O(m+n) where m and n are number of elements in the given linked lists
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode(0)  # initialize to some dummy value
        current = answer
        carry = 0
        while (l1 is not None or l2 is not None):
            if l1 is None:
                x1 = 0
            else:
                x1 = l1.val

            if l2 is None:
                x2 = 0
            else:
                x2 = l2.val

            digit = x1 + x2 + carry
            if digit > 9:
                digit %= 10
                carry = 1
            else:
                carry = 0

            current.next = ListNode(digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # In case there is carry in the last digit and there are no digits in the end e.g. 5,5  ans should be 0,1 now just 0
        if carry == 1:
            current.next = ListNode(1)
        return answer.next


# A more optimized way would be check which linked list has exhausted and then only keep adding numbers from other linked list to that list.
# We can also save further space by creating the new list by replacing one of the given list
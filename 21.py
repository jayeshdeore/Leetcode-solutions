# Merge two sorted linked lists

# This will be of O(m+n) where m and n are lengths of sorted linked lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer_list = ListNode(0)  # Initialize to some dummy value
        merged_list = answer_list

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                merged_list.next = l1
                l1, merged_list = l1.next, merged_list.next
            else:
                merged_list.next = l2
                l2, merged_list = l2.next, merged_list.next

        # The loop will break when either of the lists exhausts or both of them exhaust
        if l1 is not None:
            merged_list.next = l1

        if l2 is not None:
            merged_list.next = l2

        return answer_list.next


if __name__ == '__main__':
    my_class = Solution()
    my_list = ListNode(10)
    my_list.next = ListNode(12)
    print(my_class.mergeTwoLists(None, my_list).val)

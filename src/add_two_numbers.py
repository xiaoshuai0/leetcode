
from src.common.list_node import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        current = dummy
        carray = 0
        while l1 or l2:
            sum = carray
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            current.next = ListNode(sum % 10)
            current = current.next

            carray = sum // 10
        if carray > 0:
            current.next = ListNode(carray)

        return dummy.next

if __name__ == "__main__":
    s = Solution()

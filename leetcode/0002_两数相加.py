"""
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        str1 = ""
        while l1 is not None:
            str1 = str1 + str(l1.val)
            l1 = l1.next

        str2 = ""
        while l2 is not None:
            str2 = str2 + str(l2.val)
            l2 = l2.next

        int1 = int(''.join(str1[::-1]))
        int2 = int(''.join(str2[::-1]))

        # 807
        add = str(int1 + int2)

        l3 = l4 = ListNode(0)
        for index in range(len(add), 0, -1):
            l3.next = ListNode(int(add[index - 1]))
            l3 = l3.next

        return l4.next
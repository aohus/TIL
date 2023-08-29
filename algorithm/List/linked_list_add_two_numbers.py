"""
link : https://leetcode.com/problems/add-two-numbers
파이썬 알고리즘 인터뷰 참고
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


s = Solution()
print(s.add_two_numbers(l1=[2, 4, 3], l2=[5, 6, 4]))

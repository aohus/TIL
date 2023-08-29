"""
link: https://leetcode.com/problems/palindrome-linked-list/
파이썬 알고리즘 인터뷰 풀이 참고
    런너 기법
    - 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
    - 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다. 
    - 중간 위치를 찾아내면, 값을 비교하거나 뒤집기를 시도하는 등 활용도가 높다. 

"""
import collections
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 런너를 이용한 풀이
    def is_palindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 리스트를 만든다.
        # fast 가 두 칸씩 끝까지 가는 동안, slow는 한 칸씩 중간까지 가면서 역순 리스트(rev)를 만든다.
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # list node 가 홀수개 일 때, slow를 한 칸 옮겨서 가운데 node를 pass한다.
        # fast는 마지막 노드에 있고 fast.next는 None인 것을 이용한다.
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

    # 데크를 이용한 풀이
    def is_palindrome_deque(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

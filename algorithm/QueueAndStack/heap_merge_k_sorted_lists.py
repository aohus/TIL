from typing import List
import heapq


class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # heap 에 모든 연결 리스트의 첫 Node(=루트)를 추가한다.
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            # linked list 에 다음 원소 있으면 heap에 추가
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

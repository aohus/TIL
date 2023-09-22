"""
link: https://leetcode.com/problems/cheapest-flights-within-l-stops/
문제 : 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K 개의 경유지 이내에 도착하는 가격을 리턴하라. 경로가 존재하지 않을 경우 -1을 리턴하라.

풀이: (비용, 위치, 남은 이동)을 우선순위 Q에 넣고 도착점에 가장 처음으로 도착하는 경로의 비용을 반환한다. 우선순위 Q에 의해 최소 비용으로 더 적은 비용으로 도착하는 경로가 먼저 계산된다. 
"""
from typing import List
import collections
import heapq
import math

class Solution:
    # 마지막 시도 - 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        minHeap = [(0, src, k + 1)]  # (d, u, stops)
        dist = [[math.inf] * (k + 2) for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))

        while minHeap:
            d, u, stops = heapq.heappop(minHeap)
            if u == dst:
                return d
            if stops > 0:
                for v, w in graph[u]:
                    newDist = d + w
                    if newDist < dist[v][stops - 1]:
                        dist[v][stops - 1] = newDist
                        heapq.heappush(minHeap, (newDist, v, stops - 1))
        return -1

    # 두번째 시도 - 우선순위 큐 적용했지만 시간초과로 실패
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for from_node, to_node, price in flights:
            graph[from_node].append((to_node, price))
        
        Q = [(0, src, k)]
        while Q :
            total_price, current_node, left_move = heapq.heappop(Q)
            if current_node == dst:
                return total_price
            if left_move >= 0:
                for to_node, price in graph[current_node]:
                    heapq.heappush(Q, (total_price+price, to_node, left_move-1))
        return -1

    # 첫시도- Time Limit Exceeded로 통과 못한 답안 -> 우선순위 큐 적용해봄
    def findCheapestPrice_slow(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for from_node, to_node, price in flights :
            graph[from_node].append((to_node, price))
        
        Q = [(src, -1, 0)]
        result = []
        while Q :
            current_node, total_move, total_price = Q.pop(0)
            if total_move < k :
                for to_node, price in graph[current_node] :
                    if to_node == dst :
                        result.append(total_price+price)
                    else :
                        Q.append((to_node, total_move+1, total_price+price))
            
        if result :
            return min(result)
        return -1
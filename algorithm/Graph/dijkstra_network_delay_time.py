"""
link: https://leetcode.com/problems/network-delay-time/
문제 : K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 입력값(u,v,w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다. 

풀이: 
- 우선순위 Q와 heapq(최소 힙)을 이용하여 구현한다. 
- 시작 노드부터 BFS로 그래프를 탐색하고, Q에 인접 노드들을 등록한다. 
- Q최소 힙을 사용해서 어떤 노드 n까지 도달하는 최단 경로의 길이를 dist에 저장한다. 
"""

from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐 변수[(소요시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1

s = Solution()
print(s.networkDelayTime(times=[[3,1,5], [3,2,2], [2,1,2], [3,4,1],[4,5,1], [5,6,1],[6,7,1],[7,8,1],[8,1,1]], n=8, k=3)) # 2
# s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2) # 2
# s.networkDelayTime(times=[[1, 2, 1]], n=2, k=1) # 1
# s.networkDelayTime(times=[[1, 2, 1]], n=2, k=2) # -1
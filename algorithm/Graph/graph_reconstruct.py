"""
link: https://leetcode.com/problems/reconstruct-itinerary/
문제 : [from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우 사전 어휘 순으로 방문한다. 

풀이 : 여러 일정이 있는 경우 사전 어휘 순으로 방문해야하니, 그래프를 정렬한다. dfs로 경로를 구해 추가해준다. 
route에는 맨 마지막 호출된 dfs 스택의 노드(공항)부터 추가된다. 따라서 return 전 route를 뒤집어준다.

-> sorted(tickets) 부분을 역순으로 정렬하고(reverse=True) graph[a].pop(0)을 graph[a].pop()으로 바꾸어 스택연산을 하면 시간 복잡도가 O(n)에서 O(1)이된다.
"""
from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        
        dfs('JFK')
        return route[::-1]

s = Solution()
print(s.findItinerary([["JFK", "SFO"], ["JFK","ATL"], ["SFO","ATL"], ["ATL", "JFK"], ["ATL","SFO"]]))
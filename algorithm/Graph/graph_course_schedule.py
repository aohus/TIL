"""
link: https://leetcode.com/problems/course-schedule/
문제 : 0을 완료하기 위해서는 1을 끝내야한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다. 코스 개수 n과 이 쌍들을 입력으로 받았을 때
모든 코스가 완료 가능한지 판별하라. 

풀이: 그래프가 순환 구조인지를 판별하는 문제와 같다고 볼 수 있다. 
"""
from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for post, pre in prerequisites :
            graph[post].append(pre)
        
        def dfs(i)
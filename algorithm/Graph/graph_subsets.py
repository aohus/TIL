"""
link: https://leetcode.com/problems/subsets/
문제: 리스트가 주어지면, 리스트 원소로 만들 수 있는 모든 부분 집합의 리스트를 반환하는 함수

풀이: 시퀀스의 길이 예측할 수 없고, 원소가 겹치지 않는 subset을 만들어야하는 문제. 대표적으로 dfs 사용한다. 
list는 mutable 객체라, 하나의 list 여러 함수에 사용하기 까다롭기에 list(기존) + list(새 원소) 로 다음 dfs 함수에 넘겨준다.
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(index, path):
            answer.append(path)
            for i in range(index, len(nums)) :
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return answer
    

s = Solution()
print(s.subsets([1, 2, 3]))
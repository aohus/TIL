from typing import List 
import itertools

class Solution:
    def combineWrong(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def dfs(combine, elements):
            for e in elements :
                combine.append(e)
                if len(combine) == k :
                    answer.append(combine[:])
                    combine.pop()
                    continue                 
                next_elements = [ i for i in elements if i > e ]
                dfs(combine, next_elements)
                combine.pop()
        
        elements = [ i for i in range(1, n+1) ]
        dfs([],elements)
        return answer
    
    def combineDirty(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def dfs(elements, rest):
            for r in rest :
                elements.append(r)
                if len(elements) == k :
                    answer.append(elements[:])
                    elements.pop()
                    continue
                next = [ i for i in rest if i > r ]
                dfs(elements, next)
                elements.pop()

        elements = [ i for i in range(1, n+1) ]
        dfs([],elements)
        return answer

    def combine(self, n:int, k:int) -> List[List[int]]:
        answer=[]
        def dfs(elements, start: int, k: int):
            if k == 0 :
                answer.append(elements[:])
                return
            for i in range(start, n+1):
                # elements.append(i)
                # dfs(elements, i+1, k-1)
                # elements.pop()
                dfs(elements+[i], i+1, k-1)
        dfs([],1,k)
        return answer

    def combineTools(self, n, k):
        return list(itertools.combinations(range(1,n+1), k))
S=Solution()
print(S.combineWrong(5,3))
# print(S.combine(3,2))
# print(S.combineTools(3,2))
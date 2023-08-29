from typing import List 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        def dfs(elements:List[int], start:int) :
            if sum(elements) == target :
                answer.append(elements[:])
                return 
            if sum(elements) > target :
                return
            
            for i in candidates[start:]:
                elements.append(i)
                dfs(elements, candidates.index(i))
                elements.pop()
        dfs([],0)
        return answer
    
    def combinationSumFast(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        def dfs(csum, index, path) :
            if csum ==  0:
                answer.append(path)
                return 
            if csum < 0 :
                return
            
            for i in range(index, len(cantidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
        dfs(target,0,[])
        return answer
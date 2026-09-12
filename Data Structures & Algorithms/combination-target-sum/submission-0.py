class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        ans = []

        def findCombinations(candidates, target, arr, index):

            if target == 0:
                ans.append(arr.copy())
                return

            if target < 0 or index == n:
                return
            
            arr.append(candidates[index])
            findCombinations(candidates, target - candidates[index], arr, index)
            arr.pop()
            findCombinations(candidates, target, arr, index + 1)
        
        findCombinations(candidates, target, [], 0)

        return ans
            
            
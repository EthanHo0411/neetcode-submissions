class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i ,cur, total):
            # base case would be if our current total equal to the target
            #in that case we would simply add the curr subset as a valid result
            if total == target:
                res.append(cur.copy())
                return

            #we also have to make sure that we are not out of bound and our total is smaller than target to continue
            if i>=len(candidates) or total>target:
                return 
            
            #we will first handle the case when we include this number
            cur.append(candidates[i])

            #include the num by once
            dfs(i+1, cur, total+candidates[i])

            cur.pop()
            #not include the num
            #skips through all index with the same num , so that we dont just exclude a specific num
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cur , total)
        dfs(0,[],0)
        return res


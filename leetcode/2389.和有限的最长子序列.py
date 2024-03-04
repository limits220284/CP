class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        nums.sort()
        ans=[]
        for x in queries:
            i = 0
            cnt = 0
            while i < n:
                cnt += nums[i]
                if cnt > x:
                    break
                i += 1
            ans.append(i)
        return ans
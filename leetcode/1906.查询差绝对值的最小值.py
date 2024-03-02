class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        idxs = [[] for _ in range(max(nums) + 1)]
        for i, x in enumerate(nums):
            idxs[x].append(i)
        ans = [inf] * len(queries)
        for q, [x, y] in enumerate(queries):
            tmp = []
            for i in range(1, len(idxs)):
                arr = idxs[i]
                if not arr: continue
                l = bisect_left(arr, x)
                r = bisect_right(arr, y)
                if l < r:
                    tmp.append(i)
            if len(tmp) == 1:
                ans[q] = -1
            else:
                for a, b in pairwise(tmp):
                    ans[q] = min(ans[q], b - a)
        return ans
        
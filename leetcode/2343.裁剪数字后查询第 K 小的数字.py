class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        m,n=len(nums),len(queries)
        answer=[]
        for i in range(n):
            arr=[]
            for j in range(m):
                k=queries[i][1]
                arr.append([nums[j][-k:],j])
            arr.sort()
            answer.append(arr[queries[i][0]-1][1])
        return answer
                
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans,n=0,len(matrix)
        pr_que=[]
        for i in range(n):
            for j in range(n):
                heapq.heappush(pr_que,matrix[i][j])
        return heapq.nsmallest(k,pr_que)[-1]
                
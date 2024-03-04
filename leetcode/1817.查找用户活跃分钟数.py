class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans=[0]*k
        du=defaultdict(set)
        for x,y in logs:
            du[x].add(y)
        for x in du:
            ans[len(du[x])-1]+=1
        return ans
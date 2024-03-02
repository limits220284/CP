class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = set([0])
        def dfs(x):
            vis.add(x)
            for y in rooms[x]:
                if y not in vis:
                    dfs(y)
        for x in rooms[0]:
            if x not in vis:
                dfs(x)
        print(vis)
        return len(vis) == n
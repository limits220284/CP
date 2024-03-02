class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        g = [[set(), set()] for _ in range(n)]
        for i, x in enumerate(parent):
            if x == -1: continue
            g[x][0].add(i)
            g[i][1].add(x)
        self.g = g
        self.vis = [-1] * n


    def lock(self, num: int, user: int) -> bool:
        if self.vis[num] == -1:
            self.vis[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.vis[num] == user:
            self.vis[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.vis[num] != -1: return False
        def dfs1(x, flag):
            if self.vis[x] != -1:
                return True
            for y in self.g[x][flag]:
                if dfs1(y, flag):
                    return True
            return False
        flag1 = dfs1(num, 0)
        flag2 = dfs1(num, 1)
        def dfs2(x):
            if self.vis[x] != -1:
                self.vis[x] = -1
            for y in self.g[x][0]:
                dfs2(y)
        if flag1 and not flag2:
            dfs2(num)
            self.vis[num] = user
            return True
        return False
            

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
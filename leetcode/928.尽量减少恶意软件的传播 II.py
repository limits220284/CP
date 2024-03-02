class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # 目的是为了找到u只被u感染一次的节点个数
        # 如果把u去掉，这个数目越大，代表最后的结果越少
        n = len(graph)
        clean = set(range(n)) - set(initial)
        # 先找到initial中每个点能够直接感染的节点，就是ini不通过其他感染点感染的
        def dfs(x, vis):
            for i in range(n):
                if graph[x][i] == 1 and i not in vis and i in clean:
                    vis.add(i)
                    dfs(i, vis)
        infect_by = defaultdict(list)
        for v in initial:
            vis = set()
            dfs(v, vis)
            for t in vis:
                infect_by[t].append(v)
        # 如果该节点仅被一个节点污染，那么对应的节点+1
        infect_one = defaultdict(int)
        for k, lb in infect_by.items():
            if len(lb) == 1:
                infect_one[lb[0]] += 1
        # 找到最大的这个只感染一个节点的ini即可
        print(infect_one)
        idx, mx = min(initial), -1
        for k, v in infect_one.items():
            if v >  mx or (v == mx and k < idx):
                mx, idx = v, k
        return idx
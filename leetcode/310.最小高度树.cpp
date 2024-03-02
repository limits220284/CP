// height0 表示子树高
// height 表示树高

class Solution {
public:
    // dfs1 计算以 0 号节点为根的树中，以各个节点为根的子树高
    void dfs1(vector<vector<int>>& graph, vector<int>& height0, int u) {
        height0[u] = 1;
        int h = 0;
        for (int v : graph[u]) {
            if (height0[v] != 0) continue;
            dfs1(graph, height0, v);
            h = max(h, height0[v]);
        }
        height0[u] = h + 1;
    }

    // dfs2 进行换根动态规划，计算出所有的树高
    void dfs2(vector<vector<int>>& graph, vector<int>& height0, vector<int>& height, int u) {
        // 计算子树高的最大值和次大值
        int first = 0;
        int second = 0;
        for (int v : graph[u]) {
            if (height0[v] > first) {
                second = first;
                first = height0[v];
            } else if (height0[v] > second)
                second = height0[v];
        }
        // height[u] = first + 1;
        for (int v : graph[u]) {
            // 树高已计算，跳过这个节点
            if (height[v] != 0) continue;
            // 更新以当前节点为根的子树高，换根到 v
            height0[u] = (height0[v] != first ? first : second) + 1;
            // 这句代码和前面的 height[u] = first + 1 保留一个即可
            height[v] = max(height0[v], height0[u] + 1);
            // 递归进行换根动态规划
            dfs2(graph, height0, height, v);
        }
    }

    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (const auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        vector<int> height0(n, 0);
        vector<int> height(n, 0);
        dfs1(graph, height0, 0);
        dfs2(graph, height0, height, 0);
        vector<int> ans;
        int h = n;
        for (int i = 0;i < n;++i) {
            if (height[i] < h) {
                h = height[i];
                ans.clear();
            }
            if (height[i] == h)
                ans.push_back(i);
        }
        return ans;
    }
};
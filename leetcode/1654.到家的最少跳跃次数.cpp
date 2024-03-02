class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        // 最远距离 bound = max(F + a + b, x + b)
        int F = *max_element(forbidden.begin(), forbidden.end()), bound = max(F + a + b, x + b);

        int ban[bound + 1];
        memset(ban, 0, sizeof(ban));
        for(int f : forbidden) {
            ban[f] = 1;
        }

        int dist[bound + 1][2]; // dist[i][0] - 上一次前跳, dist[i][1] - 上一次后跳
        memset(dist, 0x3f, sizeof(dist));
        dist[0][0] = 0;
        queue<pair<int,int>> q({{0, 0}});
        while(q.size()) {
            auto [i, pre] = q.front(); q.pop();
            if(i == x) {
                return dist[i][pre];
            }
            if(pre == 0 && i-b >= 0 && !ban[i-b] && dist[i][pre] + 1 < dist[i-b][1]) {
                dist[i-b][1] = dist[i][pre] + 1;
                q.emplace(i-b, 1);
            }
            if(i+a <= bound && !ban[i+a] && dist[i][pre] + 1 < dist[i+a][0]) {
                dist[i+a][0] = dist[i][pre] + 1;
                q.emplace(i+a, 0);
            }
        }

        return -1;
    }
};
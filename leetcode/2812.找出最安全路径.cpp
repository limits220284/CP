// class Solution {
// using pii = pair<int,int>;
// public:
//     int maximumSafenessFactor(vector<vector<int>>& grid) {
//         int n = grid.size();
//         queue<pii> q;
//         vector<vector<int>> dist(n,vector<int>(n,1e9));
        
//         for(int i=0;i<n;++i){
//             for(int j=0;j<n;++j){
//                 if(grid[i][j] == 1){
//                     dist[i][j] = 0;
//                     q.push({i,j});
//                 }
//             }
//         }
        
//         int dx[4] = {-1,0,1,0},dy[4] = {0,1,0,-1};
//         while(q.size()){
//             auto [x,y] = q.front();
//             q.pop();
//             for(int i=0;i<4;++i){
//                 int nx = x + dx[i],ny = y + dy[i];
//                 if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
//                 if(dist[nx][ny] > dist[x][y] + 1){
//                     dist[nx][ny] = dist[x][y] + 1;
//                     q.push({nx,ny});
//                 }
//             }
//         }
        
        
//         // for(int i=0;i<n;++i){
//         //     for(int j=0;j<n;++j){
//         //         cout << dist[i][j] << " ";
//         //     }
//         //     cout << endl;
//         // }
        
//         int p[n*n];
//         for(int i=0;i<n*n;++i){
//             p[i] = i;
//         }
        
//         vector<int> g[2*n+1];
        
//         for(int i=0;i<n;++i){
//             for(int j=0;j<n;++j){
//                 g[dist[i][j]].push_back(i * n + j);
//             }
//         }
        
//         function<int(int)> find = [&](int x){
//             if(p[x] != x){
//                 return p[x] = find(p[x]);
//             }
//             return p[x];
//         };
        
//         for(int i=2*n-2;i>=0;--i){
//             for(int j=0;j<g[i].size();++j){
//                 auto x = g[i][j] / n,y = g[i][j] % n;
//                 for(int d=0;d<4;++d){
//                     int nx = x + dx[d],ny = y + dy[d];
//                     if(nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] >= dist[x][y]){
//                         int fa = find(x * n + y),fb = find(nx * n + ny);
//                         if(fa != fb){
//                             p[fa] = fb;
//                         }
//                     }
//                 }
//             }
//             if(find(0) == find(n * n - 1)){
//                 return i;
//             }
//         }
//         return 0;
//     }
// };

using PII=pair<int, int>;
vector<PII> dir4{{-1,0},{1,0},{0,-1},{0,1}};
PII operator+(PII a, PII b){return{a.first+b.first,a.second+b.second};}

class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dis(n, vector<int>(n, INT_MAX));
        
        queue<pair<int, int>> q;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) {
                    q.push({i, j});
                    dis[i][j] = 0;
                }
            }
        }
        
        while (!q.empty()) {
            auto [i, j] = q.front(); q.pop();
            for (auto& d : dir4) {
                auto [x, y] = d + make_pair(i, j);
                if (x >= 0 && x < n && y >= 0 && y < n) {
                    if (dis[x][y] < INT_MAX) continue;
                    dis[x][y] = dis[i][j] + 1;
                    q.push({x, y});
                }
            }
        }
        //定义一个堆，存放距离和点的坐标，然后跑dijkstra
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, less<tuple<int, int, int>>> pq;
        pq.push({dis[0][0], 0, 0});
        vector<vector<bool>> v(n, vector<bool>(n));
        
        int ans = INT_MAX;
        while (!pq.empty()) {
            auto [di, i, j] = pq.top(); pq.pop();
            if (v[i][j]) continue;
            
            v[i][j] = true;
            ans = min(ans, di);
            if (i == n - 1 && j == n - 1) return ans;
            
            for (auto& d : dir4) {
                auto [x, y] = d + make_pair(i, j);
                if (x >= 0 && x < n && y >= 0 && y < n) {
                    if (v[x][y]) continue;
                    pq.push({dis[x][y], x, y});
                }
            }
        }
        return 0;
    }
};
/*
 * @Date: 2023-05-07 00:01:11
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-05-07 00:12:37
 * @FilePath: \871(div.4)\E.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;
int m, n;
int inx[4] = {1, -1, 0, 0};
int iny[4] = {0, 0, -1, 1};

int dfs(vector<vector<int>>& g, int x, int y){
    int ans = 0;
    ans += g[x][y];
    g[x][y] = 0;
    for(int i = 0; i < 4; i++){
        int dx = x + inx[i], dy = y + iny[i];
        if(dx >= 0 && dx < m && dy >= 0 && dy < n && g[dx][dy]){
            ans += dfs(g, dx, dy);
        }
    }
    return ans;
}

void solve(){
    int t;
    cin >> t;
    while(t--){
        cin >> m >> n;
        vector<vector<int>> g(m, vector<int>(n, 0));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                cin >> g[i][j];
            }
        }
        int ans = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(g[i][j]){
                    ans = max(ans, dfs(g, i, j));
                }
            }
        }
        cout << ans << endl;
    }

}
int main(){
    solve();
    return 0;
}
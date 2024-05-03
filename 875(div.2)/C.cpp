#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
#include<climits>
#include<queue>
using namespace std;


const int N = 100010;
typedef long long ll;


void solve(){
    int n;
    cin >> n;
    vector<vector<int>> g(n);
    map<pair<int, int>, int> mp;
    for(int i = 0; i < n-1; i++){
        int a, b;
        cin >> a >> b;
        a--, b--;
        mp[{a, b}] = i+1;
        mp[{b, a}] = i+1;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    queue<pair<int, int>> que;
    que.push({-1, 0});
    mp[{-1, 0}] = -1;
    int ans = 1;
    vector<int> f(n, 0);
    f[0] = 1;
    while(!que.empty()){
        int m = que.size();
        for(int i = 0; i < m; i++){
            auto t = que.front();
            que.pop();
            int x = t.second;
            for(auto y: g[x]){
                if(f[y] != 0) continue;
                f[y] = f[x] + (mp[{x, y}] < mp[t]? 1: 0);
                que.push({x, y});
            }
        }
    }
    for(auto& x: f){
        ans = max(ans, x);
    }
    cout << ans << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
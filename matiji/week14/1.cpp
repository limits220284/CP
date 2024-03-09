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

//手写prim算法
class DSU{
public:
    DSU(int _n){
        n = _n;
        p.resize(n);
        sz.assign(n, 1);
        for(int i = 0; i < n; i++){
            p[i] = i;
        }
    }
    int find(int x){
        if(x != p[x]){
            p[x] = find(p[x]);
        }
        return p[x];
    }
    void merge(int a, int b){
        a = find(a), b = find(b);
        if(a == b) return;
        if(sz[a] > sz[b]){
            swap(a, b);
        }
        p[a] = b;
        sz[b] += sz[a];
    }
private:
    int n;
    vector<int> p;
    vector<int> sz;
};

void solve(){
    int n, k;
    cin >> n >> k;
    //prim算法
    vector<vector<int>> edges;
    while(k--){
        int i, j, c;
        cin >> i >> j >> c;
        i--, j--;
        edges.push_back({i, j, c});
    }
    sort(edges.begin(), edges.end(), [&](auto a, auto b){
        return a[2] < b[2];
    });
    DSU uf(n);
    int ans = 0;
    for(auto& e: edges){
        int a = uf.find(e[0]), b = uf.find(e[1]);
        if(a == b) continue;
        uf.merge(e[0], e[1]);
        ans += e[2];
    }
    cout << ans << endl;

}
int main(){
    solve();
    return 0;
}
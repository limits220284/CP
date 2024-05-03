#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
#include<climits>
using namespace std;


const int N = 100010;
typedef long long LL;

class UnionFindSet{
    vector<int> p;
    vector<int> rank;
    int n;
    vector<int> sz;
 
public:
    UnionFindSet(int _n){
        n = _n;
        p.resize(n);
        rank.resize(n, 0);
        sz.resize(n, 1);
        for(int i = 0; i < n; i++){
            p[i] = i;
        }
    }
    int find(int x){
        return x == p[x] ? x : p[x] = find(p[x]);
    }
    bool merge(int x, int y){
        int fx = find(x), fy = find(y);
        if(fx == fy) return false;
        if(rank[fx] < rank[fy])
            swap(fx, fy);
        p[fy] = fx;
        rank[fx] += rank[fy];
        sz[fx] += sz[fy];
        return true;
    }
};

void solve(){
    int n, m;
    cin >> n >> m;
    vector<UnionFindSet> uf(m, UnionFindSet(n));
    for(int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        a--,b--,c--;
        uf[c].merge(a, b);
    }
    int q;
    cin >> q;
    while(q--){
        int u, v;
        cin >> u >> v;
        u--, v--;
        int ans = 0;
        //遍历所有的并查集,然后寻找是否连通
        for(int i = 0; i < m; i++){
            int fu = uf[i].find(u), fv = uf[i].find(v);
            if(fu == fv){
                ans += 1;
            }
        }
        cout << ans << endl;
    }

}
int main(){
    solve();
    return 0;
}
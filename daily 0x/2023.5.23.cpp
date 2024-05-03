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
typedef long long ll;
const int MOD = 1e9 + 7;

class UnionFindSet{
public:
    vector<int> p;
    vector<int> rank;
    int n;
    vector<int> sz;

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

ll qmd(ll a, int k, int p){
    int res = 1;
    while(k){
        if(k&1){
            res = res * a % p;
        }
        k >>= 1;
        a = a * a % p;
    }
    return res;
}

void solve(){
    int n, k;
    cin >> n >> k;
    UnionFindSet uf(n);
    for(int i = 0; i < n-1; i++){
        int a, b, c;
        cin >> a >> b >> c;
        a--, b--;
        if(c == 0) uf.merge(a, b);
    }
    int ans = qmd(n, k, MOD);
    for(int i = 0; i < n; i++){
        if(uf.find(i) == i){
            ans = (ans - qmd(uf.sz[i], k, MOD) + MOD) % MOD;
        }
    }
    cout << ans;
}
int main(){
    solve();
    return 0;
}
#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<vector>
#include<climits>
#include<queue>
#include<map>
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
    int n;
    cin >> n;
    vector<int> a(n+1, 0);
    for(int i = 1; i <= n; i++){
        cin >> a[i];
    }
    vector<int> _in(n+1, 0);
    vector<int> _out(n+1, 0);
    UnionFindSet uf(n+1);
    for(int i = 1; i <= n; i++){
        uf.merge(i, a[i]);
        _out[i] += 1;
        _in[a[i]] += 1;
    }
    int mx = 0;
    map<int, vector<int>> mp;
    for(int i = 1; i <= n; i++){
        int fa = uf.find(i);
        mp[fa].push_back(i);
        if(fa == i){
            mx += 1;
        }
    }
    int noc = 0;
    for(auto& t: mp){
        if(t.second.size() == 2){
            noc += 1;
        }
        else{
            for(int x: t.second){
                if(_in[x] == 0){
                    noc += 1;
                }
            }
        }
    }
    cout << mx - (max(noc-1, 0)) << " "<< mx << endl;
    
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
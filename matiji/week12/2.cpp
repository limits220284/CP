#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<vector>
#include<climits>
using namespace std;


const int N = 1000010;
typedef long long LL;
int MOD = 1e9 + 7;

int tr[N];
LL a[N];
int n;
vector<LL> pre_c;

int lowbit(int x){
    return x & -x;
}

int query(int x){
    LL res = 0;
    for(int i = x; i; i-= lowbit(i)){
        res += tr[i];
    }
    return res;
}

void update(int x, int c){
    for(int i = x; i <= n; i += lowbit(i)){
        tr[i] += c;
    }
}

LL find(LL x){
    int l = 0, r = n-1;
    while(l < r){
        int mid = l + (r - l) / 2;
        if(pre_c[mid] >= x){
            r = mid;
        }
        else{
            l = mid + 1;
        }
    }
    return l;
}

void solve(){
    int m, t;
    cin >> m >> t;
    for(int i = 0; i < m; i++){
        cin >> a[i];
    }
    vector<LL> pre(1, 0);
    for(int i = 0; i < m; i++){
        pre.push_back(pre.back()+a[i]-t);
    }
    pre_c = pre;
    sort(pre_c.begin(), pre_c.end());
    pre_c.erase(unique(pre_c.begin(), pre_c.end()), pre_c.end());
    LL ans = 0;
    n = pre_c.size();
    for(int i = 1; i <= m; i++){
        int y = find(pre[i]) + 1;
        ans = (ans + query(y)) % MOD;
        update(y, 1);
    }
    cout << ans;

}
int main(){
    solve();
    return 0;
}

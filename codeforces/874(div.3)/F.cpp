#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<vector>
#include<climits>
#include<map>
using namespace std;

typedef long long ll;

const int N = 100010;

int qmd(int a, int k, int p){
    int res = 1;
    while(k){
        if(k&1){
            res = (ll)res * a % p;
        }
        a = (ll)a * a % p;
        k >>= 1;
    }
    return res;
}

void solve(){
    int mod = 1e9 + 7;
    map<int, int> mp;
    int n, m;
    cin >> n >> m;
    vector<int> a;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        a.push_back(x);
        mp[x] += 1;
    }
    //去重
    sort(a.begin(), a.end(), less<int>());
    a.erase(unique(a.begin(), a.end()), a.end());
    //双指针
    ll t = 1;
    int ans = 0;
    for(int i = 0; i < a.size(); i++){
        t = (t * mp[a[i]]) % mod;
        if(i >= m-1 && a[i] - a[i-m+1] < m){
            ans = (ans + t) % mod;
            t = t * qmd(mp[a[i-m+1]], mod - 2, mod) % mod;
        }
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
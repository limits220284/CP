#include<iostream>
#include<algorithm>
#include<unordered_map>
#include<set>
#include<vector>
#include<cstring>
#include<climits>
using namespace std;


const int N = 5000010;
typedef long long LL;

LL a[N];

void add(int l, int r, int c){
    a[l] += c;
    a[r+1] -= c;
}

void solve(){
    int n, m;
    cin >> n >> m;
    memset(a, 0, sizeof a);
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        add(i+1, i+1, x);
    }
    while(m--){
        int l, r, c;
        cin >> l >> r >> c;
        add(l, r, c);
    }
    LL mi = LONG_LONG_MAX;
    for(int i = 1; i <= n; i++){
        a[i] += a[i-1];
        mi = min(a[i], mi);
    }
    cout << mi;
}
int main(){
    solve();
    return 0;
}
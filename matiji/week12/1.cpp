#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<vector>
#include<climits>
using namespace std;


const int N = 100010;
typedef long long LL;

LL a[N];
LL pre[N];
int n, m;

bool check(double mid){
    for(int i = 1; i <= n; i++){
        pre[i] = pre[i-1] + a[i-1] - mid;
    }
    LL mi = 0;
    for(int i = m; i <= n; i++){
        mi = min(mi, pre[i-m]);
        if(pre[i] >= mi){
            return true;
        }
    }
    return false;
}

void solve(){
    //这题的二分答案有点巧妙
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        LL x;
        cin >> x;
        x *= 1000;
        a[i] = x;
    }
    LL l = 0, r = 1e12;
    while(l < r){
        LL mid = (l + r + 1) / 2;
        if(check(mid)){
            l = mid;
        }
        else{
            r = mid-1;
        }
    }
    cout << l << endl;
}
int main(){
    solve();
    return 0;
}
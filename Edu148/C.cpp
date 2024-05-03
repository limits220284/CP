#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
#include<stack>
using namespace std;


const int N = 100010;
typedef long long LL;


void solve(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    //去重
    a.erase(unique(a.begin(), a.end()), a.end());
    if(a.size() == 1){
        cout << 1 << endl;
        return;
    }
    int ans = 2;
    //统计波峰和波谷
    for(int i = 1; i < a.size()-1; i++){
        if(a[i-1] > a[i] && a[i] < a[i+1]){
            ans += 1;
        }
        if(a[i-1] < a[i] && a[i] > a[i+1]){
            ans += 1;
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
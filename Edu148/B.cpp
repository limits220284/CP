#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;


void solve(){
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    //前缀和
    vector<LL> arr(1, 0);
    for(int i = 0; i < n; i++){
        arr.push_back(arr.back()+a[i]);
    }
    LL ans = 0;
    for(int i = 0; i <= k; i++){
        int l = i * 2, r = n-1-(k-i);
        ans = max(arr[r+1] - arr[l], ans);
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
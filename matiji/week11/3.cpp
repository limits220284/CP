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
    int n, d;
    cin >> n >> d;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    int ans = 0;
    int l = 0;
    for(int r = 0; r < n; r++){
        while(l < r && arr[r] - arr[l] > d){
            l += 1;
        }
        ans += r - l;
    }
    cout << ans;
}
int main(){
    solve();
    return 0;
}
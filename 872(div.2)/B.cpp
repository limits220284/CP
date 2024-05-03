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
    //贪心的放置,只考虑(0,0), (0,1), (1,0) 三个点
    //要么就是最大加上两个最小, 要么就是最小加上两个最大
    int t;
    cin >> t;
    while(t--){
        int m, n;
        cin >> m >> n;
        int t = m * n;
        vector<int> arr(t);
        for(int i = 0; i < t; i++){
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());
        int ans1 = (arr[t-1]-arr[1]) * (n-1) + (t-n) * (arr[t-1]-arr[0]);
        int ans2 = (arr[t-1]-arr[1]) * (m-1) + (t-m) * (arr[t-1]-arr[0]);
        int ans3 = (arr[t-2]-arr[0]) * (m-1) + (t-m) * (arr[t-1]-arr[0]);
        int ans4 = (arr[t-2]-arr[0]) * (n-1) + (t-n) * (arr[t-1]-arr[0]);
        cout << max(max(ans1, ans2), max(ans3, ans4)) << endl;
    }

}
int main(){
    solve();
    return 0;
}
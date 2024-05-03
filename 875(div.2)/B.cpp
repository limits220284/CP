#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
#include<climits>
#include<queue>
using namespace std;


const int N = 100010;
typedef long long ll;


void solve(){
    int n;
    cin >> n;
    vector<int> a(n+1, 0), b(n+1, 0);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        cin >> b[i];
    }
    //计算a中连续数字的最大长度
    int pre = a[0];
    int cnt = 0;
    vector<int> mpa(2*n+1, 0);
    for(int i = 0; i <= n; i++){
        if(a[i] == pre){
            cnt += 1;
        }
        else{
            mpa[pre] = max(mpa[pre], cnt);
            pre = a[i];
            cnt = 1;
        }
    }
    pre = b[0];
    cnt = 0;
    vector<int> mpb(2*n+1, 0);
    for(int i = 0; i <= n; i++){
        if(b[i] == pre){
            cnt += 1;
        }
        else{
            mpb[pre] = max(mpb[pre], cnt);
            pre = b[i];
            cnt = 1;
        }
    }
    int ans = 0;
    for(int i = 1; i <= 2 * n; i++){
        ans = max(ans, mpa[i] + mpb[i]);
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
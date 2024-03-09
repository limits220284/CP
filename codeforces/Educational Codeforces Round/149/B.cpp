#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
#include<climits>
using namespace std;


const int N = 100010;
typedef long long ll;


void solve(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    s += '*';
    //找最长的< 或者>即可
    char pre = '/';
    int cnt = 0;
    int mx = 0;
    for(int i = 0; i <= n; i++){
        if(s[i] == pre){
            cnt += 1;
        }
        else{
            mx = max(mx, cnt);
            pre = s[i];
            cnt = 1;
        }
    }
    cout << mx + 1 << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
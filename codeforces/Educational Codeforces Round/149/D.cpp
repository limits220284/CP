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
    vector<int> pre(1, 0);
    for(int i = 0; i < n; i++){
        if(s[i] == '('){
            pre.push_back(pre.back() - 1);
        }
        else{
            pre.push_back(pre.back() + 1);
        }
    }
    if(pre.back() != 0){
        cout << -1 << endl;
        return;
    }
    vector<int> ans(n, 0);
    for(int i = 1; i <= n; i++){
        if(pre[i] > 0){
            ans[i-1] = 1;
        }
        else if(pre[i] == 0){
            ans[i-1] = ans[i-2];
        }
        else{
            ans[i-1] = 2;
        }
    }
    set<int> st(ans.begin(), ans.end());
    cout << st.size() << endl;
    if(st.size() == 1){
        for(int i = 0; i < n; i++){
            cout << 1 << " ";
        }
        cout << endl;
        return;
    }
    for(auto& x:ans){
        cout << x << " ";
    }
    cout << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
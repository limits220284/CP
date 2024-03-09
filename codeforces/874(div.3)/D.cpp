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

vector<int> op(vector<int>& a, int l, int r){
    int n = a.size();
    vector<int> ans;
    for(int i = r+1; i < n; i++) ans.push_back(a[i]);
    for(int i = r; i >= l; i--) ans.push_back(a[i]);
    for(int i = 0; i < l; i++) ans.push_back(a[i]);
    return ans;
};

void solve(){
    //贪心
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    if(n == 1){
        cout << a[0] << endl;
        return;
    }
    int x = find(a.begin(), a.end(), n) - a.begin();
    if(x == 0 && n > 1){
        x = find(a.begin(), a.end(), n-1) - a.begin();
    }
    vector<int> ans;
    int r = x - 1;
    int l = r - 1;
    while(l >= 0){
        if(a[l] > a[0]) l -= 1;
        else break;
    }
    l += 1;
    ans = op(a, l, r);
    ans = max(ans, op(a, x, x));

    for(auto& x: ans){
        cout << x << " ";
    }
    cout << endl;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; 
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
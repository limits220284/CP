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


void solve(){
    int n;
    cin >> n;
    vector<int> odd, even;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        if(x % 2) odd.push_back(x);
        else even.push_back(x);
    }
    if(odd.empty() || even.empty()){
        cout << "Yes" << endl;
        return;
    }
    sort(odd.begin(), odd.end());
    sort(even.begin(), even.end());
    if(odd.front() < even.front()){
        cout << "YES" << endl;
        return;
    }
    cout << "NO" << endl;

}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
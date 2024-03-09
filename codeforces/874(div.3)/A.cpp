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
    string s;
    cin >> s;
    set<string> st;
    int ans = 0;
    for(int i = 0; i < n-1; i++){
        st.insert(s.substr(i, 2));
    }
    cout << st.size() << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
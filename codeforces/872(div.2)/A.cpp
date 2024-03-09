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
    // 左右开始遍历,然后从右边找到第一个和开头不符合的位置即可
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        int n = s.size();
        set<char> st;
        for(int i = 0; i < n; i++){
            st.emplace(s[i]);
        }
        if(st.size() == 1){
            cout << -1 << endl;
        }
        else{
            cout << n-1 << endl;
        }
    }
}
int main(){
    solve();
    return 0;
}
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
    //如果是偶数,只要不都是一个字母,输出yes
    //如果是奇数,只要不是除了中间的,其他都一样,输出yes
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        int l = 0, n = s.size();
        set<char> st;
        while(l < n / 2){
            st.emplace(s[l]);
            l += 1;
        }
        if(st.size() == 1){
            cout << "NO" << endl;
        }
        else{
            cout << "YES" << endl;
        }
    }
}
int main(){
    solve();
    return 0;
}
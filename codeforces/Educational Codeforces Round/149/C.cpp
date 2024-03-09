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
    string s;
    cin >> s;
    int n = s.size();
    for(int i = 0; i < n; i++){
        if(s[i] == '?'){
            if(i == 0){
                s[i] = '0';
            }
            else{
                s[i] = s[i-1];
            }
        }
    }
    cout << s << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
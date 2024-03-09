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
    int a, m;
    cin >> a >> m;
    int t = m;
    int x = a;
    while(t--){
        if(x % m == 0){
            cout <<  "Yes";
            return;
        }
        x += x % m;
    }
    cout << "No";
}
int main(){
    solve();
    return 0;
}
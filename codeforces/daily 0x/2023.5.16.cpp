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
    int n;
    cin >> n;
    int odd = 0;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        if(x & 1){
            odd += 1;
        }
    }
    if((((odd + 1) / 2) & 1) == 0 || (odd & 1 && (n-odd) & 1)){
        cout << "Alice" << endl;
    }
    else{
        cout << "Bob" << endl;
    }
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
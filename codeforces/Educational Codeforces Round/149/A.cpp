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
    int n, k;
    cin >> n >> k;
    if(n % k){
        cout << 1 << endl << n << endl;
        return;
    }
    cout << 2 << endl << n-1 << endl <<  1 << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
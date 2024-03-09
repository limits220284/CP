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
    // l =< (k + n * y - t * x) <= r
    // 求是否存在这样的n
    //eg.1 1 <= (8 + n * 4 - 2 * 6) <= 10
    int k, l, r, t, x, y;
    cin >> k >> l >> r >> t  >> x >> y;
    bool flag = true;
    while(t--){
        if(k + y <= r){
            k += y;
        }
        k -= x;
        if(k < l){
            cout << "No";
            return;
        }
    }
    cout << "Yes";
}
int main(){
    solve();
    return 0;
}
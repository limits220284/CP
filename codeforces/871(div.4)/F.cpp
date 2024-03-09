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
    int t;
    cin >> t;
    while(t--){
        int x, y;
        int n, m;
        cin >> n >> m;
        vector<int> IN(n+1, 0);
        for(int i = 0; i < m; i++){
            int a, b;
            cin >> a >> b;
            IN[a] += 1;
            IN[b] += 1;
        }
        int a = 0;
        for(int i = 1; i <= n; i++){
            if(IN[i] == 1){
                a += 1;
            }
        }
        //算出x
        x = m - a;
        y = (2 * m - x - a) / x - 1;
        cout << x  << " "<< y << endl;
    }
}
int main(){
    solve();
    return 0;
}
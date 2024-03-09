#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
#include<climits>
#include<queue>
using namespace std;


const int N = 100010;
typedef long long ll;


void solve(){
    int n;
    cin >> n;
    vector<int> a;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        cout << n + 1 - x << " ";
    }
    cout << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
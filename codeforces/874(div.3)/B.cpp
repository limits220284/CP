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
    int n, k;
    cin >> n >> k;
    //带着下标进行排序
    vector<pair<int, int>> a;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        a.push_back({x, i});
    }
    sort(a.begin(), a.end());
    vector<int> b(n, 0);
    for(int i = 0; i < n; i++){
        cin >> b[i];
    }
    sort(b.begin(), b.end());
    vector<int> c(n, 0);
    for(int i = 0; i < n; i++){
        c[a[i].second] = b[i];
    }
    for(int i = 0; i < n; i++){
        cout << c[i] << " ";
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


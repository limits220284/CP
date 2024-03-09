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
    int m, n;
    cin >> m >> n;
    vector<int> arr;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            int x;
            cin >> x;
            arr.push_back(x);
        }
    }
    int k;
    cin >> k;
    int t = arr.size();
    while(k--){
        arr.insert(arr.begin(), arr[t-1]);
    }

    for(int i = 0; i < m; i++, puts("")){
        for(int j = 0; j < n; j++){
            cout << arr[i*n + j] << " ";
        }
    }
}

int main(){
    solve();
    return 0;
}
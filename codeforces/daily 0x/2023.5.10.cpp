#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 200010;
typedef long long LL;
int n, m;
int a[N];
bool check(int mid){
    LL res = 0;
    for(int i = 0; i < n; i++){
        res += max((a[i] - i/mid), 0);
    }
    return res >= m;
}

void solve(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    //降序排序
    sort(a, a+n, greater<int>());
    int l = 1, r = 1e9;
    while(l < r){
        int mid = (l + r) / 2;
        if(check(mid)){
            r = mid;
        }
        else{
            l = mid + 1;
        }
    }
    if(l == 1e9){
        cout << -1 << endl;
    }
    else{
        cout << l << endl;
    }
}
int main(){
    solve();
    return 0;
}
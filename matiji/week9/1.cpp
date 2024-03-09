/*
 * @Date: 2023-04-27 20:32:28
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-27 20:41:55
 * @FilePath: \week9\1.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 200010;
typedef long long LL;

int a[N];

void solve(){
    int n, c;
    cin >> n >> c;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a, a+n);
    unordered_map<int, int> cnt;
    LL ans = 0;
    for(int i = 0; i < n; i++){
        ans += cnt[a[i]-c];
        cnt[a[i]] += 1;
    }
    cout << ans;
}
int main(){
    solve();
    return 0;
}
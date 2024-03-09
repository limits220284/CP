/*
 * @Date: 2023-04-23 20:25:56
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-23 20:45:05
 * @FilePath: \week8\2.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
#include<stack>
using namespace std;


const int N = 10010;
typedef long long LL;

int a[N];
int l[N];
int r[N];
void solve(){
    //维护左边比他更大的数和右边比它更大的数
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) cin >> a[i];
    int mx = INT_MIN;
    for(int i = 0; i < n; i++){
        mx = max(mx, a[i]);
        l[i] = mx;
    }
    mx = INT_MIN;
    for(int i = n-1; i >= 0; i--){
        mx = max(mx, a[i]);
        r[i] = mx;
    }
    int ans = 0;
    for(int i = 0; i < n; i++){
        ans += min(l[i], r[i]) - a[i];
    }
    cout << ans;
}
int main(){
    solve();
    return 0;
}
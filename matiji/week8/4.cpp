/*
 * @Date: 2023-04-20 19:43:59
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-20 20:11:31
 * @FilePath: \week8\4.cpp
 */
#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<vector>
#include<cmath>
using namespace std;


const int N = 1010;
typedef long long LL;


double a[N];//账户资金
double b[N];//账户警界值

void solve(){
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; i++) cin >> a[i];
    memset(b, 0, sizeof b);
    double ans = 0;
    for(int i = 1; i <= m; i++){
        int x, y;
        double z;
        cin >> x >> y >> z;
        if(a[x] < z) break;
        double t = z - int(z);
        ans += t;
        b[y] += t;
        a[x] -= z;
        a[y] += int(z);
        if(b[y] > 1) break;
    }
    printf("%.2lf", ans);
}
int main(){
    solve();
    return 0;
}
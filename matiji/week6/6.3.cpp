/*
 * @Date: 2023-04-05 23:38:40
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-05 23:58:09
 * @FilePath: \matiji\6.3.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;

int a[N];

void solve(){
    int n,k;
    cin >> n >> k;
    for(int i = 0; i < n; i++) scanf("%d", &a[i]);
    sort(a, a + n, greater<int>());
    int ans = 0;
    int last = a[k-1];
    for(int i = 0; i < n; i++){
        if(a[i] >= last) ans += 1;
    }
    cout << ans <<endl;

}
int main(){
   solve();
   return 0;
}
/*
 * @Date: 2023-05-06 22:49:42
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-05-06 22:54:15
 * @FilePath: \871(div.4)\B.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 110;
typedef long long LL;

// int a[N];


void solve(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int m;
        cin >> m;
        int mx = 0;
        int x;
        int cnt = 0;
        for(int j = 0; j < m; j++){
            cin >> x;
            if(x == 1){
                mx = max(mx, cnt);
                cnt = 0;
            }
            else{
                cnt += 1;
            }
        }
        mx = max(mx, cnt);
        cout << mx << endl;
    }

}
int main(){
    solve();
    return 0;
}
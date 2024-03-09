/*
 * @Date: 2023-04-20 19:32:05
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-20 19:42:04
 * @FilePath: \week8\5.cpp
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


void solve(){
    int a, m;
    cin >> a >> m;
    LL x = a;
    bool flag = false;
    for(int i = 1; i <= m; i++){
        if(x % m == 0){
            flag = true;
            break;
        }
        else{
            x += x % m;
        }
    }
    if(flag) cout << "Yes";
    else cout << "No";
}
int main(){
    solve();
    return 0;
}
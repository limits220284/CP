/*
 * @Date: 2023-04-28 11:09:33
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-28 11:13:15
 * @FilePath: \week9\5.cpp
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

int h[N];

void solve(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        h[x] += 1;
    }
    int mx = -1;
    for(int i = 0; i < n; i++){
        if(h[i] != 0 && h[i] >= i){
            mx = i;
        }
    }
    cout << mx;
}
int main(){
    solve();
    return 0;
}
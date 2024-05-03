/*
 * @Date: 2023-05-06 22:42:37
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-05-07 20:14:16
 * @FilePath: \871(div.4)\A.cpp
 */
/*
 * @Date: 2023-05-06 22:42:37
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-05-06 22:47:04
 * @FilePath: \871(div.4)\A.cpp
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
    int n;
    cin >> n;
    string s = "codeforces";
    for(int i = 0; i < n; i++){
        string a;
        cin >> a;
        int cnt = 0;
        for(int j = 0; j < 10; j++){
            if(a[j] != s[j]){
                cnt += 1;
            }
        }
        cout << cnt << endl;
    }
}
int main(){
    solve();
    return 0;
}
/*
 * @Date: 2023-05-06 22:56:20
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-05-07 20:09:52
 * @FilePath: \871(div.4)\C.cpp
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
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int a = 1e9, b = 1e9, c = 1e9;
        for(int i = 0; i < n; i++){
            int x;
            string s;
            cin >> x >> s;
            if(s == "11"){
                a = min(a, x);
            }
            if(s == "01"){
                b = min(b, x);
            }
            if(s == "10"){
                c = min(c, x);
            }
        }
        //如果存在答案则需要进行对比
        if(a != 1e9 || b != 1e9 && c != 1e9){
            cout << min(a, b+c) << endl;
        }
        else{
            cout << -1 << endl;
        }
    }
    // int n;
    // cin >> n;
    // vector<PIS> arr;
    // for(int i = 0; i < n; i++){
    //     int m;
    //     cin >> m;
    //     vector<PIS> arr;
    //     for(int j = 0; j < m; j++){
    //         int t;
    //         string skills;
    //         cin >> t >> skills;
    //         arr.push_back({t, skills});
    //     }
    //     sort(arr.begin(), arr.end(), cmp);
    //     int ans = 0;
    //     bool vis[2] = {false};
    //     for(int k = 0; k < arr.size(); k++){
    //         string y = arr[k].second;
    //         if(y[0] == '1' && y[1] == '1'){
    //             ans = arr[k].first;
    //             break;
    //         }
    //     }
    //     int ans1 = 0;
    //     for(int k = 0; k < arr.size(); k++){
    //         string y = arr[k].second;
    //         if(y[0] == '0' && y[1] == '0'){
    //             continue;
    //         }
    //         else if(y[0] == '1' && y[1] == '1'){
    //             continue;
    //         }
    //         else if(y[0] == '1' && !vis[0]){
    //             ans1 += arr[k].first;
    //             vis[0] = true;
    //         }
    //         else if(y[1] == '1' && !vis[1]){
    //             ans1 += arr[k].first;
    //             vis[1] = true;
    //         }
    //         if(vis[0] && vis[1]){
    //             break;
    //         }
    //     }
    //     if(!vis[0] || !vis[1]){
    //         ans1 = 0;
    //     }
    //     if(ans && ans1){
    //         cout << min(ans, ans1) << endl;
    //     }
    //     else if(ans){
    //         cout << ans << endl;
    //     }
    //     else if(ans1){
    //         cout << ans1 << endl;
    //     }
    //     else{
    //         cout << -1 << endl;
    //     }
    // }
}
int main(){
    solve();
    return 0;
}
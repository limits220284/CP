/*
 * @Date: 2023-04-28 11:02:04
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-28 11:08:56
 * @FilePath: \week9\4.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;


void solve(){
    int n;
    cin >> n;
    vector<string> a;
    map<vector<int>, int> h;
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        vector<int> alp(26, 0);
        for(auto& c: s){
            alp[c-'A'] += 1;
        }
        h[alp] += 1;
        cout << h[alp] << "ok" << endl;
    }
    //统计大写字母的个数,组成一个元组,然后存到hash表中即可
    cout  << h.size();
}
int main(){
    solve();
    return 0;
}
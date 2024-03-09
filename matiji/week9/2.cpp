/*
 * @Date: 2023-04-27 20:47:42
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-28 10:55:20
 * @FilePath: \week9\2.cpp
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
const int mod = 100003;
typedef long long LL;
typedef pair<LL, LL> PLL;

map<PLL, bool> mp;

PLL work(vector<int>& t){
    LL s = 0, p = 1;
    for(auto& x: t){
        s += x % mod;
        p *= x % mod;
    }
    return make_pair(s, p);
}

void solve(){
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++){
        vector<int> t;
        for(int j = 0; j < 6; j++){
            int x;
            cin >> x;
            t.push_back(x);
        }
        if(mp.count(work(t))){
            cout << "found." << endl;
            return;
        }
        for(int j = 0; j < 6; j++){
            LL s = 0, p = 1;
            for(int k = 0; k < 6; k++){
                s += t[(j+k)%6] % mod;
                p *= t[(j+k)%6] % mod;
            }
            PLL tt = make_pair(s, p);
            mp[tt] = true;
        }
    }
    cout << "No" << endl;
} 

int main(){
    solve();
    return 0;
}
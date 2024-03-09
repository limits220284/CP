/*
 * @Date: 2023-04-28 10:55:41
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-28 11:45:24
 * @FilePath: \week9\3.cpp
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

// JWPUDJSTVP
// VICTORIOUS
// MAMA
// ROME
// HAHA
// HEHE
// AAA
// AAA
// NEERCISTHEBEST
// SECRETMESSAGES
void solve(){
    string a, b;
    while(cin >> a >> b){
        vector<int> x(26, 0);
        vector<int> y(26, 0);
        int n = a.size();
        for(int i = 0; i < n; i++){
            x[a[i]-'A'] += 1;
            y[b[i]-'A'] += 1;
        }
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());
        if(x == y){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }
}
int main(){
    solve();
    return 0;
}
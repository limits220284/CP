//https://codeforces.com/problemset/problem/1714/E
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
    // 采用位运算进行优化
    int z = -1, m = 0;
    for(int i = 0; i < n; i++){
        int v;
        cin >> v;
        if(v % 5 == 0){
            v += v % 10;
            //存在一个5
            if(z == -1){
                z = v;
            }
            else if(v != z){
                z = -2;
            }
        }
        else{
            m |= 1 << (v % 20);
        }
    }
    if(m > 0){
        if((z == -1) && (((m & 729366) == 0) || ((m & 729366) == m))){
            //如果分组中不存在5 并且分成了第一组或者第二组
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }
    else{
        if(z != -2){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }

}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
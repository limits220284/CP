#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;

vector<string> ans;
const int N = 100010;
typedef long long LL;

//题目意思就是给定两个数字,n和m,n只能分解成2x和x,也就是3的倍数,经过有限次的分解
//能否分解出m
void print(vector<string>& ans){
    for(auto& s: ans){
        cout << s << endl;
    }
}
bool can(int n, int& m){
    if(n == m){
        return true; 
    }
    if(n < m || n % 3) return false;
    return can(n/3, m) || can(2*n /3, m);
}

void solve(){
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n >> m;
        if(can(n, m)){
            ans.push_back("Yes");
        }
        else{
            ans.push_back("No");
        }
    }
}
int main(){
    solve();
    print(ans);
    return 0;
}
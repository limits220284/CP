#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
#include<stack>
using namespace std;


const int N = 1000010;
typedef long long LL;

int tag[N];

struct Node{
    char c;
    int inx;
};

void solve(){
    string s;
    cin >> s;
    stack<Node> stk;
    int n = s.size();
    for(int i = 0; i < n; i++){
        if(!stk.empty() && stk.top().c == '(' && s[i] == ')'){
            tag[stk.top().inx] = tag[i] = 1;
            stk.pop();
        }
        else{
            stk.push({s[i],i});
        }
    }
    // 寻找最长的1
    int mx = -1;
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(tag[i] == 0){
            cnt = 0;
        }
        else{
            cnt += 1;
        }
        mx = max(mx, cnt);
    }
    // 寻找最长1的个数
    if(mx == 0){
        cout << 0 << " " << 1 <<endl;
        return;
    }
    cnt = 0;
    int ans = 0;
    // cout<<endl;
    // for(int i = 0;i < n;i++) cout << tag[i];
    for(int i = 0; i < n; i++){
        if(tag[i] == 1){
            cnt += 1;
        }
        else{
            cnt = 0;
        }
        if(cnt == mx){
            ans += 1;
        }
    }
    cout << mx << " " << ans;
}

int main(){
    solve();
    return 0;
}
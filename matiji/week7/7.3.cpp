#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
#include<queue>
using namespace std;

const int N = 100010;
typedef long long LL;

int a[N];
int b[N];
int c[N];

struct Node{
    int ida, idb, num;
    bool operator>(const Node& a) const{
        return num > a.num;
    }
} tmp;

void solve(){
    int n, m, k;
    cin >> n >> m >> k;
    priority_queue<Node, vector<Node>, greater<Node>> q;
    for(int i = 0; i < m; i++) cin >> a[i];
    for(int i = 0; i < m; i++) cin >> b[i];
    sort(a, a+m);
    sort(b, b+m);
    for(int i = 0; i < m; i++){
        q.push({i, 0, a[i]+b[0]});
    }
    for(int i = 0; i < k; i++){
        tmp = q.top(), q.pop();
        c[i] = tmp.num;
        tmp.num = a[tmp.ida] + b[++tmp.idb];
        q.push(tmp);
    }
    n -= 2;
    while(n--){
        while(!q.empty()){
            q.pop();
        }
        for(int i = 0; i < k; i++){
            a[i] = c[i];
        }
        for(int i = 0; i < m; i++) cin >> b[i];
        sort(b, b+m);
        for(int i = 0; i < k; i++){
            q.push({i, 0, a[i]+b[0]});
        }
        for(int i = 0; i < k; i++){
            tmp = q.top(), q.pop();
            c[i] = tmp.num;
            tmp.num = a[tmp.ida] + b[++tmp.idb];
            q.push(tmp);
        }
    }
    for(int i = 0; i < k; i++){
        cout << c[i] << " ";
    }
}
int main(){
    solve();
    return 0;
}
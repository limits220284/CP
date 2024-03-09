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

struct Node{
    int ida, idb, num;
    bool operator > (const Node& a) const{
        return num > a.num;
    }
}tmp;

void solve(){
    int n, k;
    cin >> n >> k;
    priority_queue<Node, vector<Node>, greater<Node>> heap;
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i < n; i++) cin >> b[i];
    sort(a, a+n);
    sort(b, b+n);
    for(int i = 0; i < n; i++){
        heap.push({i, 0, a[i] + b[0]});
    }
    for(int i = 0; i < k; i++){
        tmp = heap.top(), heap.pop();
        cout << tmp.num << " ";
        tmp.num = a[tmp.ida] + b[++tmp.idb];
        heap.push(tmp);
    }
}
int main(){
    solve();
    return 0;
}
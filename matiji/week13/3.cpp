#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
#include<climits>
#include<queue>
using namespace std;


const int N = 1010;
typedef long long ll;

struct Node{
    int val, nex;
}node[N];

int pos, n, q, curr;

void insert(int curr, int num){
    node[++pos].val = num;
    node[pos].nex = node[curr].nex;
    node[curr].nex = pos;
}
void del(int pre){
    node[pre].nex = node[node[pre].nex].nex;
}
void solve(){
    cin >> n >> q;
    if(q == 1){
        cout << n;
        return;
    }
    node[0] = {0, 1};
    node[1] = {1, 1};
    pos = 1;
    for(int i = 2; i <= n; i++){
        insert(pos, i);
    }
    while(true){
        for(int k = 1; k < q; k++){
            curr = node[curr].nex;
        }
        if(node[curr].nex == curr){
            cout << node[curr].val;
            return;
        }
        del(curr);
    }
}
int main(){
    solve();
    return 0;
}

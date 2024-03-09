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


const int N = 2e6 + 7;
typedef long long ll;


struct Node{
    ll nex, coef, expn;
}node[N];

int n, m, head, tail, pos;
ll coefA[N], expnA[N], coefB[N], expnB[N];

void insert(int curr, ll val1, ll val2){
    node[++pos].coef = val1;
    node[pos].expn = val2;
    node[pos].nex = node[curr].nex;
    node[curr].nex = pos;
    if(!node[pos].nex){
        tail = pos;
    }
}

void solve(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> coefA[i] >> expnA[i];
    }
    for(int i = 1; i <= m; i++){
        cin >> coefB[i] >> expnB[i];
    }
    int l = 1, r = 1;
    while(l <= n && r <= m){
        if(expnA[l] == expnB[r]){
            insert(tail, coefA[l] + coefB[r], expnA[l]);
            l++, r++;
        }
        else{
            if(expnA[l] < expnB[r]){
                insert(tail, coefA[l], expnA[l]);
                l++;
            }
            else{
                insert(tail, coefB[r], expnB[r]);
                r++;
            }
        }
    }
    while(l <= n){
        insert(tail, coefA[l], expnA[l]);
        l++;
    }
    while(r <= m){
        insert(tail, coefB[r], expnB[r]);
        r++;
    }
    for(int i = node[head].nex; i != 0; i = node[i].nex){
        if(node[i].coef != 0){
            cout << node[i].coef <<" "<< node[i].expn << endl;
        }
    }
}

int main(){
    solve();
    return 0;
}
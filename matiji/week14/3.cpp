#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<map>
#include<vector>
#include<climits>
#include<queue>
#define int long long
using namespace std;

const int N = 100010;

struct Node{
    int l, r, val, lz;
}tr[N * 4];
int a[N];
void build(int p, int l, int r){
    tr[p].l = l, tr[p].r = r;
    if(l == r){
        tr[p].val = a[l];
        return;
    }
    int mid = l + (r-l) / 2;
    build(p*2, l, mid);
    build(p*2+1, mid+1, r);
    tr[p].val = tr[p*2].val + tr[p*2+1].val;
}

void lazy(int p, int v){
    int s = tr[p].l, t = tr[p].r;
    tr[p].val += (t-s+1)*v, tr[p].lz += v;
}

void pushdown(int p){
    lazy(2*p, tr[p].lz);
    lazy(2*p+1, tr[p].lz);
    tr[p].lz = 0;
}


void update(int l, int r, int c, int p){
    int s = tr[p].l, t = tr[p].r;
    if(l <= s && t <= r){
        return lazy(p, c);
    }
    if(tr[p].lz && s != t){
        pushdown(p);
    }
    int mid = s + ((t-s) / 2);
    if(l <= mid){
        update(l, r, c, p*2);
    }
    if(r > mid){
        update(l, r, c, p*2+1);
    }
    tr[p].val = tr[p*2].val + tr[p*2+1].val;
}

int query(int l, int r, int p){
    int s = tr[p].l, t = tr[p].r;
    if(l <= s && t <= r){
        return tr[p].val;
    }
    if(tr[p].lz){
        pushdown(p);
    }
    int mid = s + ((t-s) / 2), sum = 0;
    if(l <= mid){
        sum = query(l, r, p*2);
    }
    if(r > mid){
        sum += query(l, r, p*2+1);
    }
    return sum;
}

void solve(){
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; i++) cin >> a[i];
    build(1, 1, n);
    while(m--){
        int op, x, y, k;
        cin >> op >> x >> y;
        if(op == 1){
            cin >> k;
            update(x, y, k, 1);
        }
        else{
            cout << query(x, y, 1) << endl;
        }
    }
}
signed main(){
    solve();
    return 0;
}
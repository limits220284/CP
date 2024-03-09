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


const int N = 100010;
typedef long long ll;

struct Node{
    int l, r;
    bool flag;
}stu[N];

int head, tail, curr, n, k, p, m, x;

void insert(int curr, int num){
    stu[num].r = stu[curr].r;
    stu[num].l = curr;
    if(stu[curr].r){
        stu[stu[curr].r].l = num;
    }
    stu[curr].r = num;
    if(!stu[num].r){
        tail = num;
    }
}

void del(int curr){
    stu[stu[curr].l].r = stu[curr].r;
    if(stu[curr].r){
        stu[stu[curr].r].l = stu[curr].l;
    }
    if(!stu[curr].r){
        tail = stu[curr].l;
    }
    stu[curr].flag = true;
}

void solve(){
    cin >> n;
    insert(head, 1);
    for(int i = 2; i <= n; i++){
        cin >> k >> p;
        if(p == 0){
            insert(stu[k].l, i);
        }
        else{
            insert(k, i);
        }
    }
    cin >> m;
    while(m--){
        cin >> x;
        if(!stu[x].flag){
            del(x);
        }
    }
    curr = stu[head].r;
    while(curr){
        cout << curr << " ";
        curr = stu[curr].r;
    }
}
int main(){
    solve();
    return 0;
}
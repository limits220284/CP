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
int nex[N], n, m;
bool step[N];

void solve(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        nex[i] = i;
    }
    while(m--){
        char op;
        int x, y;
        cin >> op >> x >> y;
        if(op == 'A'){
            if(nex[y] == x){
                nex[y] = y;
            }
            nex[x] = y;
        }
        else if(op == 'Q'){
            int temp = x;
            memset(step, 0, sizeof step);
            bool flag = true;
            while(!step[temp]){
                if(temp == y){
                    cout << "Yes" << endl;
                    flag = false;
                    break;
                }
                step[temp] = true;
                temp = nex[temp];
            }
            if(flag){
                cout << "No" << endl;
            }
        }
    }
}
int main(){
    solve();
    return 0;
}

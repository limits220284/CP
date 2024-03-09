#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<vector>

using namespace std;

const int mod = 100003;
const int N = 100003;
typedef long long LL;

struct Node{
    int val[6], next;
}insect[N];

int n, h[N], idx;

int F(int *a){
    LL sum = 0, pro = 1;
    for(int i = 0;i < 6; i++){
        sum = (sum + a[i]) % mod;
        pro = pro * a[i] % mod;
    }
    return (sum + pro) % mod;
}

bool  equal(int *a, int *b){
    for(int i = 0; i < 6; i++){
        for(int j = 0; j < 6; j++){
            bool flag =true;
            for(int k = 0; k < 6; k++){
                if(a[(i+k)%6] != b[(j+k)%6]){
                    flag = false;
                }
            }
            if(flag){
                return true;
            }
            flag = true;
            for(int k = 0; k < 6; k++){
                if(a[(i+k)%6] != b[(j-k+6)%6]){
                    flag = false;
                }
            }
            if(flag){
                return true;
            }
        }
    }
    return false;
}
bool find(int* a){
    int k = F(a);
    for(int i = h[k]; i!=-1; i = insect[i].next){
        if(equal(insect[i].val, a)){
            return true;
        }
    }
    return false;
}

void insert(int* a){
    int k = F(a);
    memcpy(insect[idx].val, a, 6 * sizeof(int));
    insect[idx].next = h[k];
    h[k] = idx;
    idx ++;
}
void solve(){
    memset(h, -1, sizeof h);
    cin >> n;
    for(int i = 0; i < n; i++){
        int a[6];
        for(int j = 0; j < 6; j++){
            cin >> a[j];
        }
        if(find(a)){
            cout << "found.";
            return;
        }
        else{
            insert(a);
        }
    }
    cout << "No";
}
int main(){
    solve();
    return 0;
}
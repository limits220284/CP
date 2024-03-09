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

//整个排列的records其实是相同的
//取出某一个,代表总得-取出的,保证取出的最小即可,计算每一个数字的records,然后取最小值
//某一个数字的records是左边比它小的数字的个数加上右边比它大的数字的个数
class FenwickTree{
public:
    FenwickTree(int _n){
        n = _n;
        tr.assign(n+1, 0);
    }
    int lowbit(int x){
        return x & -x;
    }
    ll query(int x){
        ll ans = 0;
        for(int i = x; i; i -= lowbit(i)){
            ans += tr[i];
        }
        return ans;
    }
    void update(int x, ll c){
        for(int i = x; i <= n; i += lowbit(i)){
            tr[i] += c;
        }
    }
int n;
vector<int> tr;
};

void solve(){
    int n;
    cin >> n;
    FenwickTree bt(n);
    vector<int> chg(n+1, 0);
    int mx = 0;
    for(int i = 1; i <= n; i++){
        int x;
        cin >> x;
        mx = max(mx, x);
        int y = bt.query(x-1);
        if(y == i-1){
            chg[x]--;
        }
        else if(y == i-2){
            chg[mx] += 1;
        }
        bt.update(x, 1);
    }
    int mx = INT_MIN;
    int ans = INT_MAX;
    for(int i = 1; i <= n; i++){
        if(chg[i] > mx){
            mx = chg[i];
            ans = i;
        }
    }
    cout << ans << endl;

}
int main(){
    solve();
    return 0;
}
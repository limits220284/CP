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

//给定一个长为n的a数组,和一个数k
//从a中选择k个数，并将其分割成两块，最小化两块的和
//二分答案 + 反悔堆
//首先可以想到的是二分最大值, 即问题转换成在指定最大值的情况下,左边最多能够选取多少个数，右边最多能够选取多少个数
//可以证明答案是具有单调性的,答案是mx，大于mx，可以，小于mx不行
//如何查出给定mx下，最多能够选取多少个数呢，问题转换成，在给定最大值的情况下，连续的数组最多能够选择多少个数，类似于课程表III的解法
//采用贪心的思想，使用堆进行维护，每次都加一个数进去，然后弹出最大的数，保证当前的和是小于mx即可

//check函数
bool check(vector<ll>& a, int n, int k, ll mx){
    //前后缀分解
    vector<int> pre(n+1, 0), suf(n+1, 0);
    priority_queue<ll, vector<ll>, less<ll>> hp, hs;
    ll tot = 0;
    for(int i = 0; i < n; i++){
        tot += a[i];
        hp.push(a[i]);
        while(tot > mx){
            tot -= hp.top();
            hp.pop();
        }
        pre[i+1] = hp.size();
    }
    tot = 0;
    for(int i = n-1; i >= 0; i--){
        tot += a[i];
        hs.push(a[i]);
        while(tot > mx){
            tot -= hs.top();
            hs.pop();
        }
        suf[i] = hs.size();
    }
    //从前往后遍历,看看是否存在一个点能够前面+后面的 >= k
    for(int i = 0; i <= n; i++){
        if(pre[i] + suf[i] >= k) return true;
    }
    return false;      
}
void solve(){
    int n, k;
    cin >> n >> k;
    vector<ll> a(n, 0);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    //二分答案
    ll l = 0, r = 1e18;
    while(l < r){
        ll mid = (l + r) / 2;
        if(check(a, n, k, mid)){
            r = mid;
        }
        else{
            l = mid + 1;
        }
    }
    cout << l << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
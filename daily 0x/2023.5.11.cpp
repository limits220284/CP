#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;
int n, k;
vector<int> a;
bool check(int mid){
    // 如果这个题不考虑二分,就会转换为,划分成若干个组,每个组内至少有k个数,并且从小到大的差值不能超过mx,请问这个数组是否能够做到。
    // dp来写,令f[i]表示a[0]-a[i]是否满足要求
    // f[i] = any(f[j]), 其中i-j+1 >= k 且 a[i]-a[j] <= mx
    // 这样写复杂度是N**2,需要进行优化
    // 假设f[i]是从f[j0]转移过来的,那么在计算f[i+1]的时候所要查询的区间在j0之前的就不用计算了
    // 是因为如果j0不能够转移过来,那么j0之前的也不能转移过来,所以只用计算j0之后的即可
    vector<bool> f(n+1, false);
    f[0] = true;
    int j0 = 0;
    for(int i = k-1; i < n; i++){
        //保证a[i]-a[j0] <= mid
        while(a[i] - a[j0] > mid){
            j0 += 1;
        }
        // 必须保证从k个元素之外的j转移过来,从而保证至少有k个元素
        while(j0 <= i - k + 1){
            if(f[j0]){
                f[i+1] = true;
                break;
            }
            j0 += 1;
        }
    }
    return f[n];
}
/*
1、最大值最小,二分模板
2、每一组最少有k个数,不能够贪心,只能够dp来写
*/
void solve(){
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        a.push_back(x);
    }
    sort(a.begin(), a.end());
    int l = 0, r = a[n-1] - a[0];
    while(l < r){
        int mid = l + (r-l) / 2;
        if(check(mid)){
            r = mid;
        }
        else{
            l = mid + 1;
        }
    }
    cout << l << endl;
}
int main(){
    solve();
    return 0;
}
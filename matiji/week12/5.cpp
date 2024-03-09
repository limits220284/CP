#include<iostream>
#include<algorithm>
#include<cstring>
#include<unordered_map>
#include<set>
#include<vector>
#include<climits>
using namespace std;


const int N = 100010;
typedef long long LL;

int a[N];
int sub[N];

void solve(){
    //做差分,统计差分数组中连续相同的数的个数
    int x;
    int n = 0;
    while(cin >> x){
        n += 1;
        a[n] = x;
        sub[n] = a[n] - a[n-1];
    }
    int ans = 0;
    int pre = sub[2];
    for(int i = 2; i <= n; i++){
        //直接统计相同的数字的个数,然后O(1)计算结果
        if(sub[i] == sub[pre]){
            ans += i - pre;
        }
        else{
            pre = i;
        }
    }
    cout << ans;

}
int main(){
    solve();
    return 0;
}

#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;


void solve(){
    int n, m;
    cin >> n >> m;
    int cnt1 = 0, cnt2 = 0;
    vector<int> a;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        if(x == -1){
            cnt1 += 1;
        }else if(x == -2){
            cnt2 += 1;
        }else{
            a.push_back(x);
        }
    }
    sort(a.begin(), a.end());
    a.erase(unique(a.begin(), a.end()), a.end());
    int ans = 0;
    ans = max(ans, cnt1 + int(a.size()));//开始坐的就是第一类人, 然后
    ans = max(ans, cnt2 + int(a.size()));//能坐的全部入座后,右边依次坐第二类人
    ans = min(ans, m);
    //枚举中间有固定位置的人
    for(int i = 0; i < a.size(); i++){
        //左边最多能坐多少人,首先不能够超过a[i]-1个,然后第i位入座后,通过cnt1将左边空出来的位置补齐
        int l = min(a[i]-1, i+cnt1);
        int r = min(m-a[i], int(a.size())-1-i+cnt2);
        ans = max(ans, l + r + 1);
    }
    cout << ans << endl;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
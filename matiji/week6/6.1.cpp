/*
 * @Date: 2023-04-05 17:16:50
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-12 20:28:31
 * @FilePath: \week6\6.1.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
typedef long long LL;
using namespace std;

const int N = 100010;

int a[N];

void solve(){
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    //排序找中位数
    sort(a, a+n);
    int x = a[(n+1)/2];
    LL res = 0;
    for(int i = 0; i < n; i++){
        res += abs(x - a[i]);
    }
    cout << res;
}
int main(){
   solve();
   system("pause");
   return 0;
}
/*
 * @Date: 2023-04-06 00:10:08
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-06 00:31:20
 * @FilePath: \matiji\6.5.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;

int a[N],b[N];

void solve(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    for(int i = 0; i < n; i++){
        int x;
        scanf("%d", &x);
        b[i] = a[i] - x;
    }
    sort(b, b+n);
    int l = 0, r = n-1;
    while(l < r){
        if(b[l] < 0 && b[r] > 0 && abs(b[l]) == b[r]){
            l += 1, r -= 1;
            continue;
        }
        else{
            cout << "NO";
            return;
        }
        l += 1, r -= 1;
    }
    cout << "YES";
}
int main(){
   solve();
   system("pause");
   return 0;
}
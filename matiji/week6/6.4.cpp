/*
 * @Date: 2023-04-06 00:30:22
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-06 00:52:59
 * @FilePath: \matiji\6.4.cpp
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

 void solve(){
    int n;
    int a[N], b[N];
    int check[N];
    int even = 0, odd = 0;
    cin >> n;
    for(int i = 0; i < n; i++){
        int x;
        scanf("%d", &x);
        if(x % 2 == 0) a[even++] = x;
        else b[odd++] = x;
        check[i] = x%2;
    }
    sort(a, a + even);
    sort(b, b + odd);
    int l = 0, r = 0;
    for(int i = 0; i < n; i++){
        if(check[i] == 1){
            printf("%d ", b[r++]);
        }
        else{
            printf("%d ", a[l++]);
        }
    }
 }
 int main(){
    solve();
    return 0;
 }
/*
 * @Date: 2023-04-05 23:01:31
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-05 23:12:15
 * @FilePath: \matiji\6.2.cpp
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
unordered_map<char, int> mp;
bool cmp(char a, char b){
   return mp[a] < mp[b];
}
void solve(){
   for(int i = 0; i < 26; i++){
      char c;
      cin >> c;
      mp[c] = i;
   }
   string a;
   cin >> a;
   sort(a.begin(), a.end(), cmp);
   cout << a;
}
int main(){
   solve();
   system("pause");
   return 0;
}
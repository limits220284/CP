/*
 * @Date: 2023-04-20 19:21:48
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-23 20:54:23
 * @FilePath: \week8\1.cpp
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

struct Car{
    int ID;
    int x;
    int f;
}car[1010];

bool cmp1(Car a, Car b) {return a.x <= b.x; }
bool cmp2(Car a, Car b) {return a.ID <= b.ID;}
int n, t, tmp[1010];
void solve(){
    cin >> n >> t;
    for(int i = 0; i < n; i++){
        cin >> car[i].x >> car[i].f;
        car[i].ID = i+1;
    }
    sort(car, car+n, cmp1);
    for(int i = 0; i < n; i++){
        tmp[i] = car[i].ID;
        car[i].x = car[i].x + car[i].f * t;
    }
    sort(car, car + n, cmp1);
    for(int i = 0; i < n; i++){
        car[i].ID = tmp[i];
        if(i < n-1 && car[i].x == car[i+1].x || i > 0 && car[i].x == car[i-1].x){
            car[i].f = 0;
        }
    }
    sort(car, car+n, cmp2);
    for(int i = 0; i < n; i++, puts("")){
        cout << car[i].x << " " << car[i].f;
    }
}
int main(){
    solve();
    return 0;
}
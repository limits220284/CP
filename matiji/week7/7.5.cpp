/*
 * @Date: 2023-04-13 16:19:57
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-13 19:02:47
 * @FilePath: \week7\7.5.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
#include<deque>
using namespace std;


const int N = 100010;
typedef long long LL;


deque<int> que;

void solve(){
    int n;
    cin >> n;
    while(n--){
        int op, x;
        cin >> op;
        switch (op){
        case 1 :
            cin >> x;
            que.push_front(x);
            break;
        case 2:
            cin >> x;
            que.push_back(x);
            break;
        case 3:
            cout<< que.front() << endl;
            break;
        case 4:
            cout << que.back() << endl;
            break;
        case 5:
            que.pop_front();
            break;
        case 6:
            que.pop_back();
            break;
        default:
            break;
        }
    }
}
int main(){
    solve();
    return 0;
}
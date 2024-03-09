/*
 * @Date: 2023-04-12 20:25:09
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-13 11:27:39
 * @FilePath: \week7\7.1.cpp
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

vector<int> s;
vector<int> s_mn;

void c(int x){
    s.push_back(x);
    if(s_mn.empty()){
        s_mn.push_back(x);
    }
    else{
        int y = s_mn.back();
        s_mn.push_back(min(x, y));
    }
}
void y(){
    s.pop_back();
    s_mn.pop_back();
}

int top(){
    return s.back();
}

int g_mn(){
    return s_mn.back();
}


void solve(){
    int n;
    cin >> n;
    while(n -- ){
        int a, b; 
        cin >> a;
        switch (a){
        case 1:
            cin >> b;
            c(b);
            break;
        case 2:
            y();
            break;
        case 3:
            cout << top() << endl;
            break;
        case 4:
            cout << g_mn() << endl;
            break;
        default:
            break;
        }
    }
}

int main(){
    solve();
    system("pause");
    return 0;
}
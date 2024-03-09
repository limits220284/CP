/*
 * @Date: 2023-04-20 20:13:21
 * @LastEditors: Wang Hao
 * @LastEditTime: 2023-04-20 20:49:38
 * @FilePath: \week8\3.cpp
 */
#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<queue>
#include<vector>
using namespace std;


const int N = 100010;
typedef long long LL;

//思路:每次二分找到插入点,然后将值插进去
//维护两个堆,左边保存n//2个最小值,右边保存n//2个值
//每次来一个数,如果小于左边的最大值,则将其插入,然后如果左边维护的数多于右边,将这个数弹出,然后插到右边
//如果大于右边的最小值,则先将这个数插入,然后将右边的最小值弹出,插入到右边
void solve(){
    int n;
    cin >> n;
    priority_queue<int, vector<int>, less<int>> h1;//大根堆
    priority_queue<int, vector<int>, greater<int>> h2;//小根堆
    for(int i = 0; i < n; i++){
        char c;
        int x;
        cin >> c;
        int a = h1.size(), b = h2.size();
        if(c == '+'){
            cin >> x;
            if(a == 0 || h1.top() >= x){
                h1.push(x);
                if(h1.size() == h2.size() + 2){
                    h2.push(h1.top());
                    h1.pop();
                }
            }
            else{
                h2.push(x);
                if(h2.size() == h1.size() + 1){
                    h1.push(h2.top());
                    h2.pop();
                }
            }
        }
        else{
            if(a == b){
                cout << float((h1.top() + h2.top())) / 2 << endl;
            }
            else{
                cout << h1.top() << endl;
            }
        }
    }

}
int main(){
    solve();
    return 0;
}

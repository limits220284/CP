#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<set>
#include<vector>
using namespace std;


const int N = 1010;
typedef long long LL;

int n;
int a[N][N];

void add(int x1, int y1, int x2, int y2, int c){
    a[x1][y1] += c;
    a[x2+1][y2+1] += c;
    a[x2+1][y1] -= c;
    a[x1][y2+1] -= c;
}

void solve(){
    int m;
    cin >> n >> m;
    while(m--){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        add(x1, y1, x2, y2, 1);
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            a[i][j] += a[i][j-1] + a[i-1][j] - a[i-1][j-1];
            cout << a[i][j] << " "; 
        }
        cout << endl;
    }
}
int main(){
    solve();
    return 0;
}

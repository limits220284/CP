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
    int n, L;
    cin >> n >> L;
    vector<double> arr;
    for(int i = 0; i < n; i++){
        double x;
        cin >> x;
        arr.push_back(x);
    }
    sort(arr.begin(), arr.end());
    double mx = max(arr[0], L - arr[n-1]);
    for(int i = 0; i < n; i++){
        mx = max(mx, (arr[i+1]-arr[i])/2);
    }
    printf("%.2lf", mx);
}
int main(){
    solve();
    return 0;
}
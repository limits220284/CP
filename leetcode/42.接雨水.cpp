const int N = 20010;
int r[N];//维护右边最大值
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int mx = INT_MIN;
        for(int i = n-1; i >= 0; i--){
            mx = max(mx, height[i]);
            r[i] = mx;
        }
        mx = INT_MIN;
        int ans = 0;
        for(int i = 0; i < n; i++){
            mx = max(mx, height[i]);
            ans += (max(0, min(mx, r[i])-height[i]));
        }
        return ans;
    }
};
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> q;
        for(auto& x: nums){
            int l = 0, r = q.size()-1;
            while(l < r){
                int mid = (l + r) / 2;
                if(q[mid] >= x){
                    r = mid;
                }
                else{
                    l = mid + 1;
                }
            }
            if(q.empty() || q[l] < x) q.push_back(x);
            else q[l] = x;
        }
        return q.size();
    }
};
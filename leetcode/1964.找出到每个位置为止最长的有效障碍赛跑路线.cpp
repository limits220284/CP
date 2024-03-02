class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& nums) {
        //lcs问题的变种
        int n = nums.size();
        vector<int> q;
        vector<int> ans;
        for(int i = 0; i < n; i++){
            int l = 0, r = q.size() - 1;
            while(l < r){
                int mid = (l + r) / 2;
                if(q[mid] > nums[i]){
                    r = mid;
                }
                else{
                    l = mid + 1;
                }
            }
            if(q.empty() || q[l] <= nums[i]){
                q.push_back(nums[i]);
                ans.push_back(q.size());
            }
            else{
                q[l] = nums[i];
                ans.push_back(l+1);
            }
        }
        return ans;
    }
};
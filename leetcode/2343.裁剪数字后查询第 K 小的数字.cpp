class Solution {
public:
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        int m = nums.size(), n = queries.size();
        vector<int> answer;
        for (int i = 0; i < n; i++) {
            vector<pair<string,int>> num_c;
            for (int j = 0; j < m; j++) {
                string a =nums[j].substr(nums[j].size()-queries[i][1], nums[j].size());
                num_c.push_back({ a,j });
            }
            stable_sort(num_c.begin(),num_c.end());
            answer.push_back(num_c[queries[i][0] - 1].second);
        }
        return answer;
    }
};
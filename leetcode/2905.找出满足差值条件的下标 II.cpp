class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int idf, int vdf) {
        int n = nums.size();
        std::set<std::pair<int, int>> st;

        for (int i = 0; i < n - idf; ++i) {
            int j = i + idf;
            st.insert(std::make_pair(nums[i], i));

            if (std::abs(st.begin()->first - nums[j]) >= vdf) {
                return {st.begin()->second, j};
            }

            if (std::abs(std::prev(st.end())->first - nums[j]) >= vdf) {
                return {std::prev(st.end())->second, j};
            }
        }

        return {-1, -1};
    }
};
class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(int x:nums){
            mp[x]++;
        }
        int cnt=0,sy=0;
        for(auto [x,y]:mp){
            cnt+=y/2;
            sy+=y%2;
        }
        return {cnt,sy};
    }
};
class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int n = nums.size();
        map<int, int> mpl, mp;
        for(int i = 0; i < n; i++) mp[nums[i]] += 1;
        //因为只含有一个支配元素,所以是给定的
        int z = 0, mx = 0;
        for(auto& t: mp){
            if(t.second > mx){
                mx = t.second;
                z = t.first;
            }
        }
        cout << z << endl;
        int cnt = 0;
        for(int i = 0; i < n-1; i++){
            if(nums[i] == z){
                cnt += 1;
                mx -= 1;
            }
            if(cnt * 2 > i + 1 && mx * 2 > (n-i-1)){
                return i;
            }
        }
        return -1;
    }
};
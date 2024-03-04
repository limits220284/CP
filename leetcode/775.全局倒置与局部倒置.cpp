class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        int n=nums.size();
        int cnt=0;
        for(int i=0;i<n;i++){
            if(abs(nums[i]-i)>1){
                return false;
            }
        }
        return true;
    }
};
int v[4000];
class Solution {
public:
    long long countQuadruplets(vector<int> &nums) {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n=nums.size();
        long long sum=0;
        memset(v,0,sizeof(v));
        for(int i=2;i<n;i++){
            int z=0;
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    sum+=v[j];
                    z++;
                }else{
                    v[j]+=z;
                }
            }
        }
        return sum;
    }
};


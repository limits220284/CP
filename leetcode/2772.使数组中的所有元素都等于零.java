class Solution {
    public boolean checkArray(int[] nums, int k) {
        int n = nums.length;
        int[] f = new int[n+2];
        for(int i = 1; i <= n; i++){
            if(i == 1) f[i] = nums[i-1];
            else f[i] = nums[i-1] - nums[i-2];
        }
        for(int i = 0; i < n-k+1; i++){
            int x = f[i+1] + f[i];
            if(x < 0) return false;
            f[i+1] = 0;
            f[i+1+k] += x;
        }
        for(int i = 1; i <= n; i++){
            if(f[i] != 0) return false;
        }
        return true;
    }
}
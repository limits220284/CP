class Solution {
    int ans = 0;

    static int gcd(int a, int b){
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
    //枚举所有两两组合可能,保存其gcd,注意是组合，排列会超时。
    void dfs(List<Integer> l,int beginIndex,int k, int[] nums, boolean[] flag) {
        /*
        l：保存所有两个数的gcd值
        beginIndex: 下一组数的第一个数开始枚举的下标，保证枚举序列按照第一个数的下标升序，
        例 [3,4,6,8,7,9]
        (3, 4) -> (6, 8) -> (7, 9)
        (3, 4) -> (6, 7) -> (8, 9)
        (3, 4) -> (6, 9) -> (8, 7)
        (3, 6) -> (4, 8) -> (7, 9)
        (3, 6) -> (4, 7) -> (8, 9)
        ....
        k: 当前枚举的组数
        flag: 标记数字是否使用

         */
        if ( k * 2 == nums.length) {
            ArrayList<Integer> t = new ArrayList(l);
            Collections.sort(t);//将gcd从小到大排序

            int sum = 0;
           for(int i = 0; i < t.size(); i++){
               sum += (i + 1) * t.get(i);
           }
            ans = Math.max(ans, sum);
            return;
        }
        int idx = beginIndex;
        while (flag[idx] == true)
            idx++;
        flag[idx] = true;
        for(int i = idx + 1; i < nums.length; i++){
            if(flag[i] == false){
                flag[i] = true;
                l.add(gcd(nums[idx], nums[i]));
                dfs(l,idx + 1, k + 1, nums, flag);
                flag[i] = false;
                l.remove(l.size() - 1);
            }
        }
        flag[idx] = false;
    }
    public int maxScore(int[] nums) {
        dfs(new ArrayList<>(), 0, 0, nums, new boolean[nums.length]);
        return ans;

    }
}
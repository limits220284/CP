use std::collections::HashSet;

impl Solution {
    pub fn smallest_missing_value_subtree(parents: Vec<i32>, nums: Vec<i32>) -> Vec<i32> {
        let n = parents.len();
        let mut ans = vec![1; n];
        let mut node = match nums.iter().position(|&x| x == 1) {
            Some(i) => i as i32,
            None => return ans, // 不存在基因值为 1 的点
        };

        // 建树
        let mut g = vec![vec![]; n];
        for i in 1..n {
            g[parents[i] as usize].push(i);
        }

        // 遍历 x 子树
        fn dfs(x: usize, g: &Vec<Vec<usize>>, vis: &mut HashSet<i32>, nums: &Vec<i32>) {
            vis.insert(nums[x]); // 标记基因值
            for &son in &g[x] {
                if !vis.contains(&nums[son]) {
                    dfs(son, g, vis, nums);
                }
            }
        }

        let mut vis = HashSet::new();
        let mut mex = 2; // 缺失的最小基因值
        while node >= 0 {
            dfs(node as usize, &g, &mut vis, &nums);
            while vis.contains(&mex) { // node 子树包含这个基因值
                mex += 1;
            }
            ans[node as usize] = mex; // 缺失的最小基因值
            node = parents[node as usize]; // 往上走
        }
        ans
    }
}

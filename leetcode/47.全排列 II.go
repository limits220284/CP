func permuteUnique(nums []int) [][]int {
    ans := [][]int{}
    path := []int{}
    vis := make([]bool, len(nums))
    var dfs func()
    dfs = func() {
        if len(path) == len(nums) {
            ans = append(ans, append([]int(nil), path...))
            return
        }
        for i := 0; i < len(nums); i++ {
            if vis[i] {
                continue
            }
            if i > 0 && nums[i] == nums[i-1] && !vis[i -1] {
                continue
            }
            path = append(path, nums[i])
            vis[i] = true
            dfs()
            vis[i] = false
            path = path[: len(path) - 1]
        }
    }
    sort.Ints(nums)
    dfs()
    return ans
}
func subsetsWithDup(nums []int) [][]int {
    ans := [][]int{}
    path := []int{}
    n := len(nums)
    var dfs func(int)
    dfs = func(start int){
        ans = append(ans, append([]int(nil), path...))
        for i := start; i < n; i++ {
            if i > start && nums[i] == nums[i-1] {
                continue
            }
            path = append(path, nums[i])
            dfs(i + 1)
            path = path[:len(path) - 1]
        }       
    }
    sort.Ints(nums)
    dfs(0)
    return ans
}
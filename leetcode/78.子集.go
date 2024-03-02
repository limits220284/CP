func subsets(nums []int) [][]int {
    //注意子集和全排列的区别，不必要非要等到数组遍历完毕才加入结果中
    ans := [][]int{}
    path := []int{}
    n := len(nums)
    var dfs func(int)
    dfs = func(start int){
        ans = append(ans, append([]int(nil), path...))
        for i := start; i < n; i++ {
            path = append(path, nums[i])
            dfs(i + 1)
            path = path[:len(path) - 1]
        }       
    }
    dfs(0)
    return ans
}
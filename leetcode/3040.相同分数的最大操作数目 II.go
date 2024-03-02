func maxOperations(nums []int) int {
    gao := func(arr []int, target int) int {
        n := len(arr)
        if n == 0 {
            return 0
        }
        f := make([][]int, n)
        for i := 0; i < n; i ++ {
            f[i] = make([]int, n)
        }
        for i := n - 2; i >= 0; i -- {
            for j := i + 1; j < n; j ++ {
                if arr[i] + arr[i + 1] == target{
                    if i + 2 > j {
                        f[i][j] = 1
                    } else {
                        f[i][j] = max(f[i + 2][j] + 1, f[i][j])
                    }
                }
                if arr[j - 1] + arr[j] == target {
                    if j - 2 < i {
                        f[i][j] = 1
                    } else {
                        f[i][j] = max(f[i][j - 2] + 1, f[i][j])
                    }
                }
                if arr[i] + arr[j] == target {
                    if i + 1 > j - 1 {
                        f[i][j] = 1
                    } else {
                        f[i][j] = max(f[i + 1][j - 1] + 1, f[i][j])
                    }
                }
            }
        }
        return f[0][n - 1]
    }
    nn := len(nums)
    return max(gao(nums, nums[0] + nums[1]), 
        max(gao(nums, nums[0] + nums[nn - 1]), 
            gao(nums, nums[nn - 1] + nums[nn - 2])))
}
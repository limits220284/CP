func goodDaysToRobBank(security []int, time int) []int {
    //前后缀分解
    n := len(security)
    left := make([]int, n)
    right := make([]int, n)
    for i := 0; i < n; i++ {
        left[i] = 1
        if i > 0 && security[i] <= security[i-1] {
            left[i] += left[i - 1]
        }
    }
    for i := n - 1; i >= 0; i-- {
        right[i] = 1
        if i < n - 1 && security[i] <= security[i + 1] {
            right[i] += right[i + 1]
        }
    }
    fmt.Println(left, right)
    ans := []int{}
    for i := 0; i < n; i++ {
        if left[i] >= time + 1 && right[i] >= time + 1 {
            ans = append(ans, i)
        }
    }
    return ans
}
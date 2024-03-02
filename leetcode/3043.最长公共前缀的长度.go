func longestCommonPrefix(arr1 []int, arr2 []int) int {
    // 通过hash表解决问题
    mp := make(map[string]struct{})
    for _, num := range arr1 {
        nums := strconv.Itoa(num)
        n := len(nums)
        for i := 0; i < n; i ++ {
            mp[nums[:i + 1]] = struct{}{}
        }
    }
    fmt.Println(mp)
    ans := 0
    for _, num := range arr2 {
        nums := strconv.Itoa(num)
        n := len(nums)
        for i := 0; i < n; i ++ {
            if _, ok := mp[nums[:i + 1]]; ok {
                ans = max(ans, i + 1)
            }
        }
    }
    return ans
}
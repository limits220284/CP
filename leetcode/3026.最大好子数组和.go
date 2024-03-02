func maximumSubarraySum(nums []int, k int) int64 {
    mp := make(map[int]int)
    n := len(nums)
    prefix := make([]int, n + 1)
    for i, x := range nums {
        prefix[i + 1] = prefix[i] + x
    }
    ans := math.MinInt
    for i, x := range nums {
        if idx, ok := mp[x - k]; ok {
            ans = max(ans, prefix[i + 1] - prefix[idx])
        }
        if idx, ok := mp[x + k]; ok {
            ans = max(ans, prefix[i + 1] - prefix[idx])
        }
        if idx, ok := mp[x]; ok {
            if prefix[i] - prefix[idx] < 0 {
                mp[x] = i
            }
        } else {
            mp[x] = i
        }
    }
    if ans == math.MinInt {
        return 0
    }
    return int64(ans)
}
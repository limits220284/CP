func longestAlternatingSubarray(nums []int, threshold int) int {
    //分组循环模板题目
    n := len(nums)
    i := 0
    ans := 0
    for i < n {
        if nums[i] % 2 != 0 || nums[i] > threshold {
            i += 1
            continue   
        }    
        start := i
        i += 1
        for i < n && nums[i] % 2 != nums[i - 1] % 2 && nums[i] <= threshold {
            i += 1
        }
        ans = max(ans, i - start)
    }
    return ans
}
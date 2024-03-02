func findTheArrayConcVal(nums []int) int64 {
    ans := 0 
    i, j := 0, len(nums) - 1
    for i < j {
        val, _ := strconv.Atoi(strconv.Itoa(nums[i]) + strconv.Itoa(nums[j]))
        ans += val
        i += 1
        j -= 1
    }
    if i == j {
        ans += nums[i]
    }
    return int64(ans)
}
func sumIndicesWithKSetBits(nums []int, k int) int {
    ans := 0
    for i := 0; i < len(nums); i++ {
        if bitCount(i) == k {
            ans += nums[i]
        }
    }
    return ans
}

func bitCount(x int) int {
    cnt := 0
    for x != 0 {
        cnt += (x % 2)
        x /= 2
    }
    return cnt
}